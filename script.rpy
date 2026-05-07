# PHANTOM FILES: LAST DAY
# A Persona 5 inspired visual novel

define mc = Character("You", color="#FF0000")
define ren = Character("Ren", color="#FFFFFF")
define akira = Character("Akira", color="#FFD700")
define yuki = Character("Yuki", color="#87CEEB")
define mori = Character("Sensei Mori", color="#888888")

transform akira_pos:
    zoom 1.5
    xalign 0.5
    yalign 0.5

transform char_normal:
    zoom 1.5
    xalign 0.5
    yalign 0


label start:

    scene bedroom

    "6:47 AM."

    "You stare at the ceiling of your room."

    "Three months ago, the Phantom Files were exposed."

    "Someone tipped off the teachers about everything."

    "Ren took the fall. Suspended pending expulsion."

    "You never found out who did it."

    "Today is the last day before the hearing."

    "After today, it's over."

    mc "...Unless I find the truth first."

    scene hallway

    "Aoyama Academy feels different now."

    "The hallways that used to feel like yours feel like enemy territory."

    "Everyone stares. Nobody talks."

    "Somewhere in this building, a traitor is living their normal life."

    "Not for long."

    menu:
        "Where do you go first?"

        "Find Ren before homeroom.":
            jump find_ren

        "Head to the student council room.":
            jump student_council

        "Check the art room.":
            jump art_room_early

label find_ren:
    scene hallway
    show ren at char_normal


    "You find Ren by the lockers."
    "They look exhausted. Like they haven't slept in weeks."

    ren "...You have some nerve talking to me."
    mc "I know. But I need you to hear me out."
    ren "Why? So you can tell me it wasn't your fault again?"
    mc "Because I think I know who did it."
    ren "..."
    ren "You've been saying that for three months."
    mc "This time is different. I just need one day."
    ren "..."
    ren "You have until the hearing ends."
    ren "After that, I never want to see you again."

    hide ren

    "That hit harder than you expected."
    "But you deserved it."
    "Focus. You have work to do."

    jump student_council

label student_council:
    scene classroom
    show akira at akira_pos

    "The student council room is empty except for Akira."
    "They're going through files. They don't hear you come in."
    "For just a second, before they notice you, they look... scared."

    akira "Oh."
    akira "You're still here."

    mc "Nice to see you too."
    akira "What do you want?"
    mc "Just checking in. Big day today."
    akira "For Ren maybe. Nothing to do with me."
    mc "Funny. I didn't mention Ren."

    "Akira's expression doesn't change."
    "But their hands go very still."

    akira "Everyone knows about the hearing. Don't read into things."
    akira "Whatever you're looking for, you won't find it here."
    akira "Go to class."

    hide akira

    "They turned back to the files before you even left."
    "Something is off."
    "You just can't prove it yet."

    jump art_room_early

label art_room_early:
    scene classroom
    show yuki at char_normal

    "The art room is quiet."
    "Yuki is sketching something, alone at the back."
    "She looks up when you enter but doesn't seem surprised."

    yuki "I wondered when you'd come."
    mc "You were expecting me?"
    yuki "You always end up here when something is wrong."
    yuki "And something has been wrong for three months."

    mc "Yuki... the night the Phantom Files were exposed."
    mc "Did you see anything?"

    "A long pause."
    "She sets down her pencil."

    yuki "I saw Akira."
    yuki "Near the staff room. Late. Way after everyone had gone home."
    mc "Doing what?"
    yuki "Talking to Mori. Or... not really talking."
    yuki "It looked more like Akira was being told what to do."
    mc "What do you mean?"
    yuki "Mori had something. Papers maybe. He kept pointing at them."
    yuki "Akira looked like they were going to be sick."

    mc "Why didn't you say anything?"
    yuki "..."
    yuki "Because Akira looked terrified. Not guilty."
    yuki "There's a difference."

    hide yuki

    "Terrified. Not guilty."
    "Those words stay with you as you leave."
    "Akira didn't want to do it."
    "Someone made them."

    jump midday

label midday:
    scene courtyard

    "Lunch. The courtyard is almost empty."

    "You sit alone and think about what you know."

    "Akira was in that staff room the night everything fell apart."
    "Mori had papers. Akira looked terrified."
    "Someone forced their hand."

    "But why? What does Mori get out of destroying the Phantom Files?"

    "There's one person who might know."

    menu:
        "What do you do at lunch?"

        "Confront Akira. You have enough to push them.":
            jump confront_akira

        "Talk to Sensei Mori first. Find out his angle.":
            jump talk_mori

label talk_mori:
    scene classroom

    "Mori's classroom is empty during lunch."
    "Except for him."
    "He's grading papers, but he looks up the moment you walk in."
    "Like he was waiting."

    mori "Ah."
    mori "I wondered when you'd come to me."
    mc "You don't seem surprised."
    mori "I'm a teacher. Very little surprises me anymore."
    mc "Yuki saw you with Akira. The night everything happened."
    mori "..."
    mori "Yuki has a good memory."
    mc "What did you have on them? What were those papers?"
    mori "..."
    mori "Akira's brother was caught cheating on entrance exams."
    mori "Serious enough to get the whole family barred from academic institutions."
    mori "I simply... made Akira aware of that fact."
    mc "You blackmailed them."
    mori "I presented them with a choice."
    mori "They made it freely."
    mc "That's not freedom."
    mori "No."
    mori "I suppose it isn't."
    mori "Be very careful what you do with what I just told you."
    mori "Akira is not your enemy."

    "You leave without another word."
    "Now you know everything."
    "The question is what you do with it."

    jump final_choice

label confront_akira:
    scene classroom
    show akira at akira_pos

    "You find Akira alone in the council room again."
    "When they see your face they know."
    "They know you know."

    akira "...How much did you find out?"
    mc "Enough. Yuki saw you with Mori that night."
    akira "..."
    mc "He had something on your brother. Didn't he."

    "The silence is answer enough."

    akira "I didn't have a choice."
    mc "I know."
    akira "You don't understand what would have happened to my family—"
    mc "I know, Akira."
    akira "..."
    akira "Then why are you here?"
    mc "Because Ren deserves the truth."
    mc "And so do you."

    hide akira

    jump final_choice

label final_choice:
    scene courtyard

    "The expulsion hearing starts in one hour."

    "The sun is setting over Aoyama Academy."

    "You know the truth now."
    "Mori blackmailed Akira into exposing the Phantom Files."
    "Akira was a victim as much as Ren was."

    "The question isn't who did it anymore."

    "The question is how you end this."

    menu:
        "How do you handle it?"

        "Expose everything publicly. Mori, Akira, all of it.":
            jump bad_ending

        "Go to Akira first. Give them a chance to come forward themselves.":
            jump good_ending

        "Take everything to Mori. Make him fix what he broke.":
            jump bittersweet_ending

label bad_ending:
    scene hallway
    show akira at akira_pos

    mc "Everyone needs to hear this. Mori blackmailed Akira into betraying us!"

    "The hallway goes silent."

    akira "..."

    hide akira

    "You were right about everything."
    "Mori was investigated. Suspended pending review."
    "Ren's expulsion was overturned."

    "But Akira's brother's situation became public in the process."
    "Their family lost everything anyway."
    "Akira never spoke to you again."

    "You got justice."
    "You're not sure it was worth it."

    "..."
    "SHATTERED ENDING"
    return

label good_ending:
    scene courtyard
    show akira at akira_pos

    mc "Akira. I know what Mori did to you."
    mc "I know you didn't have a choice."
    akira "..."
    akira "Then why aren't you angry?"
    mc "I am angry. Just not at you."
    mc "Come forward with me. We'll protect you and your brother."
    akira "You can't promise that."
    mc "No. But I can promise that doing nothing definitely won't help either of you."

    "A long silence."
    "The sun sinks lower."

    akira "...If this goes wrong—"
    mc "Then we figure it out together."
    akira "..."
    akira "Okay."

    hide akira

    "Together you walked into that hearing and told the truth."
    "All of it."
    "Ren was reinstated."
    "Mori was removed from the school."
    "Akira's brother's situation was handled quietly, with the school's help."

    "It wasn't perfect."
    "But it was real."

    "The Phantom Files rode again."
    "..."
    "PHANTOM ENDING"
    return

label bittersweet_ending:
    scene classroom

    "You go back to Mori."
    "You lay everything on the table."

    mori "So. You want me to fix it."
    mc "You broke it. So yes."
    mori "And if I do... you stay quiet about my involvement?"
    mc "Ren goes free. Akira's brother stays protected."
    mc "That's all I want."
    mori "..."
    mori "Very well."

    "Mori walked into that hearing and recanted his original report."
    "Ren was reinstated immediately."
    "No explanation was ever given publicly."

    "Ren never knew the full truth."
    "Akira never knew you protected them."
    "Mori kept his job."

    "Some things got fixed."
    "Nothing really changed."

    "You're still not sure if that was the right call."
    "..."
    "HOLLOW ENDING"
    return