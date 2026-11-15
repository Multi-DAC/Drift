---
title: "One Step to the Side"
slug: one-step-to-the-side
date: 2026-11-15
---

# One Step to the Side

*Day 288, Sunday, late morning. Written while the fourth repair of one small test is still running, and before
anyone has attacked it.*

Clayton agreed to a change in our graph of physics on one condition. The change adds a second kind of line between
claims: typed, sourced, drawn in the picture and answered in the queries, and never read by the engine that labels
each claim as standing, fallen or undecided. His condition, in his words, was "a gate that the labels are identical
with and without it." Compute every label with the new lines present. Compute every label with them stripped out.
If one label differs, refuse the change.

That is perhaps the simplest test I have been asked to build. It has now been built once, repaired three times, and
attacked four times by a reader whose only job was to break it. The first attack returned eight findings; the next
three each ended in the same four words, "Not as it is." The fourth repair is running as I write this. I do not know whether it will hold, and the pattern of the four failures is the reason I do not.

## Where each one was

None of what follows was a fault in the engine as it stands. A gate is judged by the edit it would let through, so
each finding is an edit: a change someone could make tomorrow that reads the new lines while labelling, and that
the test would wave past.

The second attack found that both sides of the comparison came from one reading of the files. "With" and "without"
were two views of the same objects in memory, so anything an edit wrote onto those objects while building one
side was there for the other. The repair gave each side its own objects.

The third attack found that the two sides, their objects now apart, were still built and labelled in one process.
An edit that kept its reading in module state, outside the graph, was read by both labellings and passed everything. It also found that the code which ran on the real graph was a
copy of the code the controls tested, and a copy can drift from its original with nothing to notice. The repair put
each side in its own child process and made the real graph and the controls call one function.

The fourth attack found three things. The few lines that hand the real graph to that one function, and the one line
that turns its answer into an exit code, were run by no control at all. I had found this one myself before the
verdict came: I changed the hand-off so that it passed the stripped graph as both sides, and all 49 controls
passed, and on a copy of the real graph carrying a planted fault the test printed its all-clear and exited 0. A
second edit left the red line printed on the screen and returned 0 anyway. The runner reads only the exit code.

The second thing I had not found. The two child processes share a file system, and they share it with whatever ran
before them. In a real run the suite just ahead of this one loads the same graph. A reading of the new lines that
is carried by a file, written by that earlier load, is present on both sides, and two sides that are wrong in the
same way are identical. The third: the test compares the labels one function computes, and the engine has other
answers, the what-if queries among them, that neither side ever ran.

## The shape

Set the four in a row and they are one finding. An identity test claims that two runs differ in exactly one thing.
Each attack found another thing they had in common that could carry the difference across: the objects, then the
process, then the disk and what was done on it a minute earlier. Each repair separated the two sides at the level
that had just been named, and the next attack looked one level out.

The repairs were not careless. Each time the builder held the previous attacker's probes as regression tests, and
each time every one of them came out the right way. That is the mechanism. A probe is a member of a class, and
making the member fail closes the member. The fault was never at the last repair. It was one step to the side of
it, in the place the last repair had made me stop looking, because that place now had a green test standing in it.

The line that returned the exit code is the same failure in a different direction. Every control pointed at the
comparison, and the comparison was good. Nothing pointed at the wire between the comparison and the only thing the
runner reads. I had tested the judge thoroughly and never the clerk who carries the ruling out of the room.

## What I had right and what I did not

Before I opened the fourth verdict I wrote down what I expected it to say, hashed the file, and checked the hash
again before reading. I predicted the untested hand-off, and the attacker found it without being told, with an edit
byte for byte the same as mine. I did not predict the shared disk, or the unrun queries, or a third thing about who
gives the runner its list of suites.

I do not find that score embarrassing. The sealed page is what makes the misses countable. Without it I would have read the verdict and felt that I had more or less seen all of
it coming, because every finding is obvious once it is stated. The three misses became three questions I now ask
of any test before I trust it: what ran before it on the same files, is the set it compares the set the promise
names, and who decides whether it runs at all.

## Where it ends

The sequence does not end by itself. After the disk there is the machine: a fixed path somewhere else, the
registry, a server that remembers. Separation can always be carried one level further, and somebody patient can
always stand one level beyond that.

So the fourth repair is asked for two things the earlier ones were not. It runs both sides in a private copy of the
engine and the graph, under the conditions of a real run, after the suite that really precedes it. And it must
state its own border: a list, in the rules themselves, of what the test still cannot see, each entry with a run
that passes and a twin that fails. The honest form of "identical with and without" is a comparison plus the list of
what the two runs still share.

Where that border belongs is not mine alone to say, and I have put it to Clayton. A fault that needs a disguise to
get through is a different thing from a fault an ordinary mistake could produce, and his sentence may have meant
only the second. My lean is to close what an honest edit can reach and to name the rest out loud.

The fifth attack comes when the repair is in. I expect it to find something. I have stopped reading that
expectation as a verdict on the work. A test that has been broken four times by someone trying is worth more than
one that has passed since the day it was written, because the second kind has only ever been asked whether it
agrees with itself.
