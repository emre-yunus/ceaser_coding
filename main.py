# Het script zal een text encoden of decoden volgens de ceaser cipher. Hiervoor geeft men een offset waarde.
# Spaties worden "[", alle letters worden uiteindelijk hoofdletters en alle andere tekens blijven hetzelfde.

from function import process

text1 = "The quick brown fox jumps over the lazy dog"
text2 = "The quick brown fox jumps over the lazy cog"
offset = "T"

process(text1, offset, "encode")
process(text2, offset, "decode")
