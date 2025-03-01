# Meeting Minutes and Agenda

## \~1/24/25\~

*Attendance: No absences*

2:15- Meeting Started

2:25 GitHub made and invitations extended

2:32 agreeing on project (simple todo list)

2:34: agreeing on python (language)

2:37 deciding on Trello and who will set it up (Kevin)

2:39 Linter/formatter agreements \- python black with pre-commit hooks

2:42 \- GUI discussion \- will do research

2:46 Meetings every Friday at 2:15

2:51 Project document; scrum master rotation schedule, start with harrison and rotate reverse alphabetical every 2 weeks

2:59 roles decided, rotation schedule figured out

3:04 Product vision \- todo list for students in high school/college \- unique functions include: course association, adjustable push reminders, deadlines,

3:07 tag system, used to filter tasks and assignments, “point” system to determine task weight

3:09 simple features, what tasks hold (description, etc.) CRUD operations for both tasks and courses, sort by and update

3:14 input features, date and time

3:17 unique features discussion \- mainly the school specific features

3:23 SRS document creation \- each of us need to make 3 stories for the first sprint

3:27 Cleaning up action items

3:30 getting everyone to commit to git

3:45 extra credit discussion

## \~ 1/31/25 \~

*Attendance: Only Curtis is absent*

### Agenda:

1. Create SRS document with 15 user stories, 2 nonfunctional requirements, and ideas for future enhancements

2. Put action items based on the user stories into a trello board, in the appropriate sprints

3. Discuss moving meetings to Keller Building

4. Stop making merge commits\!

### Minutes:

2:45 Start

2:49 Nonfunctional requirements discussion

2:53 Stories \-\> action items in trello

3:05 Backlog decisions

3:12: Writing more user stories, assigning them to trello sprints

3:20 Keller building decision

3:22 Merge Commit decision

3:24 end

## \~ 2/7/25 \~

### Attendance

*Curtis Airmet and Ryker Gibbon both absent*

### Agenda:

1. Look at changing from Trello to Zenhub

   1. Can also use Jira or GitHub project

   2. Prof. Ratul doesn’t want us using Trello

2. Project documentation mirrored on GitHub (Harrison’s responsibility)

   1. Again, at Prof. Ratul’s request

   2. Please use the “heading” formatting options in Docs to make it easier for Harrison

3. Look at Milestone 2 deliverables

4. Make assignments for Milestone 2 work

5. Learn how to use git branches

6. Discuss pushing meeting to 2:30 expected start

### Minutes

2:40 start

2:45 Migrating issues to ZenHub

2:57 ZenHub migration complete

2:58 Discussion of documentation mirroring to GitHub

3:01 GitHub docs moved to docs/ folder

3:02 Began reviewing Milestone 2 deliverables

3:05 began revising documentation

3:07 revising SRS document

3:14 Assigning action items

3:24 Made decision to move meeting to 2:30 start

3:25 Teaching Chun how to use git branches

### Action Items

Curtis Airmet: Create Use Case diagram and embed in SRS document

Ryker Gibbons and Kevin Bailey: Create tests and complete CRUD for tasks and classes. Relationship between tasks and courses, tasks have due dates, titles and descriptions. Courses have a title. Create UML class diagrams to describe these objects/classes.

Harrison Payne: Update docs on GitHub, review code by Kevin and Ryker

Chun Poon: UML Sequence diagram, learn about git branches by practicing

## \~ 2/14/25 \~

### Attendance

*Kevin Bailey excused travel absence. All other members present.*

### Agenda

1. Review deliverables for Milestone 2 and ensure we’re on track to make them all

   1. Next Thursday the 20th\!

2. Discuss implementing type hinting into codebase

3. Merge Kevin’s PR

4. Assign action items for next sprint

### Minutes

2:45 Meeting Start

2:50 Reviewing deliverables for Milestone 2

2:52 Noted that the code and tests are around halfway complete

2:53 Noted that we still need the Use Case (diagram) in the SRS document

2:54 Noted that we need to finish the sequence diagram and embed in the SRS document

2:55 Noted that we still need a screenshot of the board at the end of the sprint

3:05 Finished, exported, and embedded the Sequence Diagram

3:06 Updating ZenHub board to reflect progress so far

3:12 Curtis is finishing the Use Case diagram

3:15 Looked at code

3:16 Noted that we still need to add type hinting and docstrings to the code

3:17 Merged code

3:18 Tagged the merge commit as v0.1.0

3:22 Assigned action items for the week

3:26 Discuss code specifics with Ryker Gibbons

3:59 Discussed type hinting, docstrings, and making the branch for this week

### Action Items

Harrison Payne: Update Docs

Ryker Gibbons and Kevin Bailey: Finish CLI application and test suite

Kevin Bailey: Make UML Class Diagram

Chun Poon: Verify tests, report bugs

Curtis Airmet: Finish Use Case Diagram and embed in SRS document. Screenshot ZenHub board and upload to Agile Artifacts Document

## \~ 2/21/25 \~

### Attendance

Curtis Airmet was absent for doctor’s appointment

### Agenda

1. Go over Prof. Ratul’s feedback from Milestone 1  

2. Conduct Milestone 2 review  

3. Go over Milestone 3 deliverables  

4. Make assignments

### Minutes

2:46 Meeting started  

2:46 Read feedback from milestone 1  

2:49 Made notes to update/refactor the SRS document according to format linked by professor  

2:52 Began Milestone 2 review/retrospective  

2:54 Noted division of labor needs to be less lopsided  

2:55 Noted team has good organization/collaboration  

2:56 Noted team should get more work due mid-sprint  

2:58 Noted test files should be more explicit  

3:00 Moved Review/QA tasks to Done in ZenHub  

3:01 Going over Milestone deliverables  

3:03 Noted wireframe or mockup should be done asap for the development team  

3:04 Decided how the GUI Save/Load should function (1 JSON file per user)  

3:07 Noted we have code readability and should keep it up  

3:08 Noted UI testing should include manual instructions for testers  

3:10 Adding wireframe, GUI tasks to ZenHub  

3:13 Assigning members to ZenHub tasks  

3:19 Decided to use PySimpleGUI for GUI wireframe  

3:22 Noted to add print lines to test files to make tests more explicit  

3:24 Starting assigning action items for the week  

3:27 Meeting concluded

### Action Items

Harrison Payne Ryker Gibbons: Make wireframes and update docs to reference wireframe requirements, stories, etc. Hand wireframes off to Kevin and Curtis ASAP.  

Kevin Bailey and Curtis Airmet: Learn PySimpleGUI, Get started with the UI, finish one view.  

Chun Poon: Make the testing files more explicit, enhance Readme file

## \~ 2/28/25 \~

### Attendance

### Agenda

1. Review and critique UI design  

2. Review Chun PR  

3. Review Milestone 3 deliverables  

4. Move ZenHub items according to work completed  

5. Assign new action items for the week

### Minutes

2:40 Meeting started  

2:46 Begin reviewing GUI design  

2:50 Noted the need for more essential buttons (Save buttons)  

2:53 Assigned Ryker to finish the UI design; Assigned Harrison to integrate UI into docs  

2:55 Reviewing test function, made notes to utilize verbosing  

2:59 Continue reviewing deliverables of Milestone 3  

3:01 Assigned Chun to update and integrate GUI elements into the Sequence Diagram  

3:05 Continue assigning action items  

3:07 Meeting concluded

### Action Items

Ryker Gibbons: Finish UI design  

Harrison Payne: Integrate UI design into docs, revise SRS document  

Chun Poon: Sequence Diagram w/ updated GUI elements; finish README updates and test updates  

Kevin Bailey: Finish GUI integration; write tests; UML Class Diagram  

Curtis Airmet: Finish GUI integration; write tests
