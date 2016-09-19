#!/usr/bin/env bash
#
# ./run_queries.sh &> run_queries.txt

xsb --quietload --noprompt --nofeedback --nobanner << END_XSB_STDIN

['rules/general_rules'].
['rules/yw_rules.P'].
[yw_views].
['facts_NLTK/yw_model_facts.P'].

set_prolog_flag(unknown, fail).

%-------------------------------------------------------------------------------

banner( 'YW_Q1',
        'What is the name and description of the workflow implemented by the script?',
        'yw_q1(WorkflowName, Description)').
[user].
:- table yw_q1/2.
yw_q1(WorkflowName, Description) :-
    yw_workflow_script(WorkflowId, WorkflowName, _,_),
    yw_description(program, WorkflowId, _, Description).
end_of_file.
printall(yw_q1(_,_)).
%-------------------------------------------------------------------------------


%-------------------------------------------------------------------------------
banner( 'YW_Q2',
        'What workflow steps comprise the top-level workflow?',
        'yw_q2(StepName, Description)').
[user].
:- table yw_q2/2.
yw_q2(StepName, Description) :-
    yw_workflow_script(WorkflowId,_,_,_),
    yw_workflow_step(StepId, StepName, WorkflowId, _, _, _),
    yw_description(program, StepId, _, Description).
end_of_file.
printall(yw_q2(_,_)).

%-------------------------------------------------------------------------------

%-------------------------------------------------------------------------------
banner( 'YW_Q3',
        'Where is the definition of workflow step CountSentiments?',
        'yw_q3(SourceFile, StartLine, EndLine)').
[user].
:- table yw_q3/3.
yw_q3(SourceFile, StartLine, EndLine) :-
    yw_workflow_script(WorkflowId,_,_,_),
    yw_workflow_step(_, 'CountSentiments', WorkflowId, SourceId, StartLine, EndLine),
    yw_source_file(SourceId, SourceFile).
end_of_file.
printall(yw_q3(_,_,_)).
%-------------------------------------------------------------------------------

%-------------------------------------------------------------------------------
banner( 'YW_Q4',
        'Describe CountSentiments step?',
        'yw_q4(StepName,Description)').
[user].
:- table yw_q4/2.
yw_q4(StepName, Description) :-
    yw_workflow_script(WorkflowId,_,_,_),
    yw_workflow_step(StepId, 'CountSentiments', WorkflowId, _, _, _),
    yw_description(program, StepId, StepName, Description).
end_of_file.
printall(yw_q4(_,_)).
%-------------------------------------------------------------------------------

END_XSB_STDIN
