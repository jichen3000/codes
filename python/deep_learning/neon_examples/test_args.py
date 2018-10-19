from neon.util.argparser import NeonArgparser

parser = NeonArgparser(__doc__)
args = parser.parse_args()
print args