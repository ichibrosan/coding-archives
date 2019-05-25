# Makefile 1/6/2008 COPR doug@goodall.com

# The FLAGS may either contain a -f or not depending on whether
# you want to see the source and destination IP nunmbers as
# fully qualified domain names or dotted numerical IP numbers.
# If -f is used, dotted numerical octets will be used. Otherwise
# fully qualified domain names will be used for non-local IP numbers
# if available.

FLAGS = -f
#FLAGS = 

INTERFACE = -i en1
PACKETS = -c 32768
ROLE = sudo
SAMPLEFILE = sample.txt
TOOL = tcpdump
VERBOSITY = -v

$(SAMPLEFILE):
	$(ROLE) $(TOOL) $(FLAGS) $(PACKETS) $(INTERFACE) > $(SAMPLEFILE) 
