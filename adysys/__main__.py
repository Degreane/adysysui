from optparse import OptionParser
import sys
def parse_args():
    parser=OptionParser("adysys [options] args")
    parser.add_option('-f','--flex',dest="useflex",help="Use 'FlexBox' (optional,default=false) ",action="store_true",default=False)
    parser.add_option('-g','--grid',dest="usegrid",help="Use 'Grid' (optional,default=false)",action="store_true",default=False)
    parser.add_option('-o','--old',dest="oldbrowsers",help="Use support for old browsers (optional,default=true)",action="store_true",default=False)
    parser.add_option('-p','--project',dest="project",help="Use Project 'projectpath' (required)",type="str",action="store",nargs=1)

    parsed=parser.parse_args()
    if parsed[0].project is None:
        parser.print_help()
        sys.exit()
    return parsed[0]

cmd_args=parse_args()
