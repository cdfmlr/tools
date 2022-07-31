'''
An email (sending) client.

    Usage: email_sender.py [options]
    Options:
        -f SENDER, --from SENDER
                                Sender email address. Default: None (set by MYEMAIL_SENDER)
        -p PASSWORD, --password PASSWORD
                                Sender email password. Default: None (set by
                                MYEMAIL_PASSWORD)
        -m SMTP_HOST, --smtp SMTP_HOST
                                SMTP host. Default: None (set by MYEMAIL_SMTP_HOST)
        -t RECEIVERS, --to RECEIVERS
                                Receiver email address. Multiple receivers can be specified
                                by multiple -t options: -t receiver1 -t receiver2
        -s SUBJECT, --subject SUBJECT
                                subject, default: "No subject"
        -c CONTENT, --content CONTENT
                                content in plain text. Default: read from stdin
        -a ATTACHMENTS, --attachment ATTACHMENTS
                                attachment file path. Multiple attachments can be specified
                                by multiple -a options: -a attachment1 -a attachment2
        -S SIGNATURE, --signature SIGNATURE
                                signature, default: "<sender> <current time>"
'''

# TODO: config file: put password in env is not secure, I think.

import os
import sys
import os.path
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
import argparse


class SmtpClient(object):
    '''
    # SmtpClient 邮件发送客户端

    ### 初始化参数:

    - user:      登录 SMTP 服务的发件人地址
    - password:  发件人邮箱密码
    - smtp_host: 发件人邮箱 SMTP 服务器地址
    - smtp_port: 发件人邮箱 SMTP 服务器端口，缺省为 25

    ### 基本用法:

    ```python
    client = SmtpClient('sender@example.com', 'sender_password', 'smtp.host.com', 25)
    mail = SmtpClient.build_email(...)
    client.send(mail)
    client.close()
    ```

    更推荐使用 with as 语法：

    ```python
    mail = SmtpClient.build_email(...)
    with SmtpClient('sender@example.com', 'sender_password', 'smtp.host.com') as client:
        client.send(mail, receivers)
    ```

    ### 方法

    - send(message, receivers): 发送邮件
    - close(): 退出客户端登录

    静态方法：

    - build_email(subject, sender, receivers, content, attachments, signature) -> MIMEMultipart: 构建邮件

    '''

    def __init__(self, sender, password, smtp_host, smtp_port=465):
        '''
        SmtpClient 是一个邮件发送客户端。

        - sender:    登录 SMTP 服务的发件人地址
        - password:  发件人邮箱密码
        - smtp_host: 发件人邮箱 SMTP 服务器地址
        - smtp_port: 发件人邮箱 SMTP 服务器端口
        '''
        self.sender = sender

        self.smtp = smtplib.SMTP_SSL(smtp_host, smtp_port)
        self.smtp.login(sender, password)

    def send(self, message: MIMEMultipart, receivers: list):
        '''
        发送邮件。

        - message:   构建好的邮件，MIMEMultipart
        - receivers: 收件人列表
        '''
        self.smtp.sendmail(self.sender, receivers, message.as_string())

    def close(self):
        '''
        退出客户端登录。
        '''
        self.smtp.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @staticmethod
    def build_email(subject: str, sender: str, receivers: list, content: str, attachments: list, signature=None) -> MIMEMultipart:
        '''
        build_email 构建邮件。

        参数：

        - subject:     主题
        - sender:      发件人
        - receivers:   收件人列表
        - content:     邮件正文，html
        - attachments: 附件路径列表
        - signature:   签名，html。缺省为 None，表示由程序自动添加。

        返回：

        - message：一个 MIMEMultipart 对象
        '''
        # 新建邮件
        message = MIMEMultipart()

        # 基本信息
        message['Subject'] = subject
        message['From'] = sender
        message['To'] = ','.join(receivers)

        # 添加文本内容
        # text_content = MIMEText(content, 'html', 'utf-8')
        text_content = MIMEText(content, 'plain', 'utf-8')
        message.attach(text_content)

        # 添加附件
        for fpath in attachments:
            with open(fpath, 'rb') as f:
                part = MIMEApplication(f.read())
                part.add_header('Content-Disposition', 'attachment',
                                filename=os.path.basename(fpath))
                message.attach(part)

        # 添加签名
        if signature is None:
            signature = f'{sender}\n{time.strftime("%Y-%m-%d %H:%M:%S")}'

        signature_content = MIMEText('\n\n' + signature, 'plain', 'utf-8')
        message.attach(signature_content)

        return message


ENV_PROFIX = 'MYEMAIL_'
ENV_SENDER = ENV_PROFIX + 'SENDER'
ENV_PASSWORD = ENV_PROFIX + 'PASSWORD'
ENV_SMTP_HOST = ENV_PROFIX + 'SMTP_HOST'

default_sender = os.environ.get(ENV_SENDER)
default_password = os.environ.get(ENV_PASSWORD)
default_smtp_host = os.environ.get(ENV_SMTP_HOST)


def cli():
    """ parse command line arguments:
       * -f    => sender
       * -p    => password
       * -m    => smtp_host

       * -r -r => receivers

       * -s    => subject
       * -c    => content  (opened file)
       * -a -a => attachments
       * -S    => signature
    """
    parser = argparse.ArgumentParser(description='Send email.')
    # sender
    parser.add_argument('-f', '--from', type=str, default=default_sender, dest='sender',
                        help=f'Sender email address. Default: {default_sender} (set by {ENV_SENDER})')
    parser.add_argument('-p', '--password', type=str, default=default_password,
                        help=f'Sender email password. Default: {default_password} (set by {ENV_PASSWORD})')
    parser.add_argument('-m', '--smtp', type=str, default=default_smtp_host, dest='smtp_host',
                        help=f'SMTP host. Default: {default_smtp_host} (set by {ENV_SMTP_HOST})')
    # receiver
    parser.add_argument('-t', '--to', type=str, action='append', dest='receivers',
                        help='Receiver email address. Multiple receivers can be specified by multiple -t options: -t receiver1 -t receiver2')
    # mail content
    parser.add_argument('-s', '--subject', type=str, default='No subject',
                        help='subject, default: "No subject"')
    parser.add_argument('-c', '--content', type=argparse.FileType('r'), default=sys.stdin,
                        help='content in plain text. Default: read from stdin')
    parser.add_argument('-a', '--attachment', type=str, action='append', dest='attachments', default=[],
                        help='attachment file path. Multiple attachments can be specified by multiple -a options: -a attachment1 -a attachment2')
    parser.add_argument('-S', '--signature', type=str,
                        help='signature, default: "<sender>\n<current time>"')
    return parser.parse_args()


def check_args(args):
    necessary_args = ['sender', 'password', 'smtp_host', 'receivers']
    for arg in necessary_args:
        if not getattr(args, arg):
            print(f'ERR: {arg} is not specified.')
            sys.exit(1)


if __name__ == "__main__":
    args = cli()
    check_args(args)

    mail = SmtpClient.build_email(
        subject=args.subject,
        sender=args.sender,
        receivers=args.receivers,
        content=args.content.read(),
        attachments=args.attachments,
        signature=args.signature)

    with SmtpClient(args.sender, args.password, args.smtp_host) as client:
        client.send(mail, args.receivers)
