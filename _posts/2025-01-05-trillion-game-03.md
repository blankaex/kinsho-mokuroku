---
layout: post
title: "[ASW] Trillion Game - 03 [1080p HEVC][27B43783].mkv"
author: Blankaex
excerpt: "Hmm only 2 of them look like crackerz."
comments: true
image:
  feature: "2025-01-05-trillion-game-03.jpg"
categories:
  - review
  - fansub
---

[convex's last post]({{ site.url }}/articles/2025-01/ameku-takao-01) gave me a good laugh and got me in the mood to take off the translator hat a little bit. So we're gonna [do a desch](https://fansubbing.com/tag/code-review/) and talk about a bit of hacking.

![](https://i.imgur.com/28NCB2Y.jpeg)

Ah yes, the global tech giants—Google and NTT.

Also I once worked at a place that had a big display on the wall. It showed random traceroute hops just like the background of this screenshot, and all the engineers knew it was just a decoration and wasn't useful for anything, but the execs found it impressive so we kept it up as a bit of an in-joke.

![](https://i.imgur.com/HeFWIhb.jpeg)

To be precise he said you "infiltrate" the server, not join it. He also said you "steal the flags from each other", which I suppose is in the spirit of what you'd normally think when you hear "capture the flag" in an everyday context.

This isn't quite right in practice though because "flags" here are just sequences of letters and numbers, so you can't really take them from each other. They're not a limited resource. They're also not usually spread across the file system of a single server either. Challenges will have different interfaces (like a web page or network shell), or may not even require interacting with a server (i.e. for binary/crypto challenges). A particular challenge *might* have you gain access to a server to find a flag, but it's a bit of a stretch to describe an entire CTF event as such.

![](https://i.imgur.com/YTWFSN8.jpeg)

I find this to be a pretty strange reaction to have. It's very common to find participants trying to fuzz input fields before events even begin, so you'd expect to see a lot of nonsense. If anything, they'd be looking for people to laugh at for trying crude payloads like `' or '1'='1`.

![](https://i.imgur.com/zexymK5.jpeg)

Japan has a surprisingly abundant selection of print-media. The CS section of book stores has shown me everything from tutorials for vim and radare2 to guides on how to walk binaries and build CPUs. 

That said, you'd be hard-pressed to get much CTF practice from a book. Challenges often rely on live infrastructure that you need to interact with, so you'd best hope they're hosting it for the duration of the book's lifetime and not just expecting you to write binaries bit by bit.

Also that top-right book should probably be "Internet Security", not "Internet & Security".

![](https://i.imgur.com/wLjkkMh.jpeg)

Guy in the back seems about right. Needs more badly-fitting hoodies and furries though for it to be truly representative of reality. You should be able to smell the image.

![](https://i.imgur.com/PjcZi1z.jpeg)

Well colour me surprised. This looks heavily inspired by CTFd, which is a pretty common CTF framework used industry-wide. I'd like to think that someone using this as a reference has participated in at least a few CTFs. Let's take a look at some of the challenge categories.

![](https://i.imgur.com/uRa9RQt.jpeg)

Contrary to any preconceptions you might have, "pwn" is actually a term that's accepted in the industry. In the context of CTF challenge categories it usually refers to binary exploitation challenges. The "first stack" and "basic stack" challenge titles allude to this too, referring to the memory stack of an executing program which is a common target for this kind of challenge.

![](https://i.imgur.com/Z3CoujG.jpeg)

Crypto is short for cryptography and not for cryptocurrency and I will die on this hill alone if I have to. These challenges usually involve breaking some kind of cipher or encryption. One of the challenges refers to RSA, which is a really cool public-key cryptosystem that's founded on prime numbers and big brain math. In short: it's very easy to multiply two primes together; but given a big number, it's very hard to figure out which primes multiply together to give that result.

![](https://i.imgur.com/Wflws5L.jpeg)

Web is another standard CTF category. These challenges are usually browser-based, which should come as a surprise to nobody. Injection-based vulnerabilities are pretty common here, such as XSS and SQLI. 

My only nitpick here is "only one chance to answer this question" is not a good challenge title and breaks the convention they've already set for themselves. That rule should be included in the challenge description and in the submission logic, but I suppose they wanted to make it obvious for the viewer.

![](https://i.imgur.com/dlMgryH.jpeg)

Reversing is (not strictly, but often) one of the first steps taken to solve binary exploitation challenges. Given that there is already a "pwn" category for binary exploitation, I'm not really sure what makes these two distinct. Maybe they're binary challenges with more of a focus on the reversing aspect as opposed to say, dynamic analysis or memory manipulation. Hard to say though because the challenge names don't give much detail.

![](https://i.imgur.com/KUokkxF.jpeg)

Opening the file on frame 1, and on bare metal? Rookie mistake. Try that at Def Con and you'll probably find your file system wiped by some MP4 0-day.

![](https://i.imgur.com/ke3i5IC.jpeg)

Would be more accurate to say "around 500/100", because as you can see in the challenges they've already showed, they points are distributed across a range.

You'd also expect dynamic scoring on the challenges to mitigate against ties (i.e. flags become worth fewer points the more people submit them), but they're all static I guess because tying is part of the plot here.

![](https://i.imgur.com/C59HmUL.jpeg)

Not a "flag keyword", just a "flag". CTF flags are usually in the format `FLAG{this_is_an_example_flag}` to make them clearly distinctive from artifacts on a system (like UUIDs), and to make it obvious to participants that the solution has been found.

Also, I would've xxd'd the video file before watching it. There's always something like this in there. Very generous of the challenge creator to align the bytes so that the flag doesn't span across lines too. Here's an xxd of this blog for reference. It's just a text file so it's not very interesting.

![](https://i.imgur.com/HrHcQ2B.png)

![](https://i.imgur.com/ZC0jRm7.jpeg)

This is actually the meta strat. You usually don't benefit much by having people cooperate on a single challenge, so it's best to delegate so that you don't double-up.

I did a 24hr CTF at uni once and one of my teammates finished all of their challenges so they were just playing XIV for the rest of the time. The interviewers made up something about how it must be a "unique way of solving challenges" when they came around because they didn't want to embarrass the other schools *too* much.

![](https://i.imgur.com/KVe7Gqv.jpeg)

Finally a bit of a glimpse into what's actually going on. Immediately I'm liking the vim usage. The script he has up uses pwntools, which is a python library that provides a bunch of functions for quick and dirty exploit development.

I'll spare you the line-by-line analysis, but this is a ret2libc exploit. The script (at least, the part we can see) attempts to overflow the input buffer in order to write into the stack. The payload calls puts to locate the address of libc, which can subsequently be used for arbitrary code execution even in a protected stack. Again, very generous of the challenge creators to provide the entire libc.

As for the background window, I'm not really sure what that is. My first thought was Metasploit, but that has a different logo. MSploit is apparently a real thing but doesn't seem to have a v5.0.101—the latest release is v1.0.3. Hard to say if this has anything to do with the task at hand but I've yet to see a program with 101 patches before a minor release in the real world.

![](https://i.imgur.com/sKxS006.jpeg)
![](https://i.imgur.com/GVuxaCf.jpeg)

Dunno about that one chief. If you have two people who don't know how to do a stack overflow like the above, putting them together won't magically make them know. It's not like a riddle where you can just brainstorm answers until you get it right.

![](https://i.imgur.com/MZ1u0aG.jpeg)

See, this is what happens when you get Dunning-Kruger peaks on Zoom for your CTF. Pretty much every challenge involves exploiting vulnerabilities except like, cryptography and steganography stuff. You could at least call out what kind of vulnerability you think it is. Reminds me of convex talking about the nurse saying stomach parasite.

![](https://i.imgur.com/HWKiXg9.jpeg)
![](https://i.imgur.com/EpSfUNP.png)

Anyways, specialist topics are often (understandably) simplified or exaggerated in Hollywood, but I find the portrayal of hacking in consumer media to be especially egregious—have you seen [Numb3rs](https://www.youtube.com/watch?v=O2rGTXHvPCQ)? That being said, *Trillion Game* does a pretty good job. Borrowing convex's words from last time, it's "realistic enough for anime standards". Also the show is just pretty enjoyable in general so I'd check it out if it interests you.
