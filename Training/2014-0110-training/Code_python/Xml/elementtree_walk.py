#!/usr/bin/env python

"""Process an XML document with elementtree.

Show the document tree.
Modify the document tree and then show it again.

Usage:
    python elementtree_walk.py [options] infilename
Options:
    -h, --help      Display this help message.
Example:
    python elementtree_walk.py myxmldoc.xml
"""


#
# Imports:
import os
import sys
import getopt
import time
from xml.etree import ElementTree as etree


#
# Global variables and constants:



#
# Functions for external use, factories, etc:



#
# Classes:



#
# Functions for internal use:

def show_tree(doc):
    root = doc.getroot()
    show_node(root, 0)


def show_node(node, level):
    show_level(level)
    print 'tag: %s' % (node.tag, )
    for key, value in node.attrib.iteritems():
        show_level(level + 1)
        print '- attribute -- name: %s  value: "%s"' % (key, value, )
    if node.text:
        text = node.text.strip()
        show_level(level + 1)
        print '- text: "%s"' % (node.text, )
    if node.tail:
        tail = node.tail.strip()
        show_level(level + 1)
        print '- tail: "%s"' % (tail, )
    for child in node.getchildren():
        show_node(child, level + 1)


def show_level(level):
    for x in range(level):
        print '   ',


def modify_tree(doc, tag, attrname, attrvalue):
    root = doc.getroot()
    modify_node(root, tag, attrname, attrvalue)


def modify_node(node, tag, attrname, attrvalue):
    if node.tag == tag:
        node.attrib[attrname] = attrvalue
    for child in node.getchildren():
        modify_node(child, tag, attrname, attrvalue)


def test(docname):
    """Test the functions in this module.
    """
    doc = etree.parse(docname)
    show_tree(doc)
    print '-' * 50
    date = time.ctime()
    modify_tree(doc, 'person', 'date', date)
    show_tree(doc)


USAGE_TEXT = __doc__

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    cur_path = os.getcwd()
    print "current path",cur_path

    args = sys.argv[1:]
    print "args = ",args
    print sys.argv[2:],sys.argv[3:]


    try:
        opts, args = getopt.getopt(args, 'h', ['help',
            ])
    except:
        usage()
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
    if len(args) != 1:
        usage()
    docname = args[0]

    test(docname)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
