=====================================================
Keyword Counter using Watson Streaming Speech to Text
=====================================================

This program converts speech to text then count
how many times the keyword or the key sentence
appears in a speech via IBM Cloud Speech to Text API.

The readers are first refered to the README of
`Watson Streaming Speech to Text`_,
an example of using Watson to real time transcribe
from Speech to Text using the websockets streaming API.

Configuration
=============
The keyword is configurable in speech.cfg as well as the credentials.

Expected Output
===============
'-t' flag is to determine a timeout value. When the keyword is found, the system repeats the keyword by using 'say' command. Note that if IBM Cloud Speech to Text recognizes the 'say' command speech correctly, the system 'say's the keyword again; then it repeats to 'say' forever.

::

    [ngym@Regulus /Users/ngym/Murai-Lab/Projects/Auto-You-Know-Counter/program/stt-keyword-counter]%python3 ./stt-keyword-counter.py -t 10                                                                                                                         [12/17 10:49:54]
    * recording
    you know!
    you know!
    * done recording
    Recognized text is 'you know I have opinions you know I have a couple you now you now '
    2 'you know' have been found!!

IBM Cloud Speech to Text recognizes 'you know' of 'say' command as 'you now' hence the system does not repeat to 'say'.




.. _Watson Streaming Speech to Text: https://github.com/ibm-dev/watson-streaming-stt

