"""KeynotePresenterNotesMarkdown to text
简化 KeynotePresenterNotesToMarkdown.scpt 的输出文件。
制作逐字稿。
"""

import re
import sys

if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'h', 'help']:
    print("Usage: km2t /path/to/file.key.md")
    print('km2t: KeynotePresenterNotesMarkdown to text')
    print("简化 KeynotePresenterNotesToMarkdown.scpt 的输出文件。制作逐字稿。")
    exit(1)
filename = sys.argv[1]

pattern = '## Slide [\s\S]*? Notes:'
repl = ''  # repl = '---'

with open(filename) as f:
    t = re.sub(pattern, repl, f.read())
    with open(filename + '.txt', 'w') as o:
        o.write(t)

"""配套的 Apple Script
--==============================
-- Send Keynote Text to Desktop Markdown File
-- Writted By: Richard Dooling https://github.com/RichardDooling/
-- Based on
-- Send Keynote Presenter Notes to Evernote
-- Version 1.0.1
-- Written By: Ben Waldie <ben@automatedworkflows.com>
-- http://www.automatedworkflows.com

-- Version 1.0.0 - Initial release
-- Version 1.0.1 - Updated for Keynote 6.2 compatibility
--==============================

-- Make sure a presentation is opened in Keynote. If not, notify the user and stop.
tell application "Keynote"
	if (front document exists) = false then
		display alert "Unable to proceed." message "Please open a presentation in Keynote."
		return
	end if

	set extractBody to button returned of (display alert "Would you like to extract slide content too?" buttons {"Yes", "No"}) = "Yes"

	-- Target the front presentation.
	tell front document
		-- Get the name of the presentation.
		set thePresentationName to name

		-- Retrieve the titles of all slides.
		set theTitles to object text of default title item of every slide

		-- If specified, retrieve the body text of all slides
		if extractBody = true then
			set theBodyText to object text of default body item of every slide
		end if

		-- Retrieve the presenter notes for all slides.
		set theNotes to presenter notes of every slide
	end tell
end tell

-- Prepare the notes as Markdown.
set theFormattedNotes to "# " & "Keynote Presentation: " & thePresentationName & return & return
repeat with a from 1 to length of theTitles
	set theFormattedNotes to theFormattedNotes & "## Slide " & a & return & return
	set theFormattedNotes to theFormattedNotes & "### Title: " & item a of theTitles & return & return
	if extractBody = true then
		set theFormattedNotes to theFormattedNotes & "#### Body " & return & return & item a of theBodyText & return & return
	end if
	set theFormattedNotes to theFormattedNotes & "#### Presenter Notes: " & return & return & item a of theNotes & return & return
end repeat
set theFormattedNotes to theFormattedNotes & return


-- Replace any returns with line breaks.
set AppleScript's text item delimiters to {return, ASCII character 10}
set theFormattedNotes to text items of theFormattedNotes
set AppleScript's text item delimiters to {return, ASCII character 10}
set theFormattedNotes to theFormattedNotes as string
set AppleScript's text item delimiters to ""

set theDesktopPath to the path to the desktop folder as text
set myFile to open for access file (theDesktopPath & thePresentationName & ".md") with write permission
write theFormattedNotes to myFile as «class utf8»
close access myFile

-- tell application "TextEdit"
-- 	activate
-- 	-- Create Desktop Markdown .md file named after Presentation
-- 	set theDesktopPath to the path to the desktop folder as text
-- 	make new document with properties {text:theFormattedNotes}
-- 	save document 1 in file (theDesktopPath & thePresentationName & ".md")
-- 	close document 1
-- end tell

-- 可以配合这段 python 那些标题再去掉：
-- import re
-- filename = '/path/to/sth.key.md'
-- pattern = '## Slide [\s\S]*? Notes:'
-- repl = '==='
-- with open(filename) as f:
--     t = re.sub(pattern, repl, f.read())
--     with open(filename + '.txt', 'w') as o:
--         o.write(t)
--
"""
