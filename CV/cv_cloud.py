#!/usr/bin/env python
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""

import random
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import string

# list of skills
skills = [("C++", 5),
          ("Python", 5),
          ("Latex", 5),
          ("Arch Linux", 5),
          ("Ubuntu", 5),
          ("MacOS", 5),
          ("Cantera", 5),
          ("Git", 5),
          ("Matlab", 4),
          ("Bash", 4),
          ("CUDA", 4),
          ("MPI", 4),
          ("Slurm", 4),
          ("Docker", 4),
          ("RegEx", 4),
          ("SQL", 3),
          ("Markdown", 3),
          ("Office", 3),
          ("Windows", 3),
          ("OpenMP", 2),
          ("Java", 2),
          ("Javascript", 2),
          ("OpenCL", 2),
          ("OpenGL", 2),
          ("Haskell", 2),
          ("x86", 2),
          ("HTML", 2),
          ("CSS", 2),
          ("Fortran", 2),
          ("Ghidra", 1),
          ("Django", 1),
          ("React", 1),
          ]

word_list = [ s for s, level in skills for l in range(level) ]
random.shuffle(word_list)
text = " ".join(word_list)

print(text)
# generate mask
comp_mask = np.array(Image.open("42.png"))
# the regex used to detect words is a combination of normal words, ascii art, and emojis
# 2+ consecutive letters (also include apostrophes), e.x It's
normal_word = r"(?:\w[\w']+)"
# 2+ consecutive punctuations, e.x. :)
ascii_art = r"(?:[\w][{punctuation}][{punctuation}]+)".format(punctuation=string.punctuation)
# a single character that is not alpha_numeric or other ascii printable
emoji = r"(?:[^\s])(?<![\w{ascii_printable}])".format(ascii_printable=string.printable)
# other symbols
emoji = r"(?:[^\s])(?<![\w{ascii_printable}])".format(ascii_printable=string.printable)
regexp = r"{normal_word}|{ascii_art}|{emoji}".format(normal_word=normal_word, ascii_art=ascii_art, emoji=emoji)
# Generate a word cloud image
wordcloud = WordCloud(background_color=None, mode="RGBA", regexp=regexp, font_step=2, width=150, height=500)

cloud = wordcloud.generate(text)
# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
# plt.figure( )
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout()
# plt.show()
plt.savefig("cv-cloud-vert.pdf")

# # lower max_font_size
# wordcloud = WordCloud(max_font_size=40).generate(text)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
