#!/usr/bin/python
# MDOSHI - Maschinendeck Door Opening SHell Improved

import time, cmd, logging, sys
from subprocess import call

def unlock_door():
    call(['gpio','export','23','out'])
    time.sleep(1)
    call(['gpio','unexport','23'])
    logging.info("unlocked")
    
def lock_door():
    call(['gpio','export','22','out'])
    time.sleep(1)
    call(['gpio','unexport','22'])
    logging.info("locked")

class MDOSHI(cmd.Cmd):
    prompt = '>> '
    undoc_header = None 

    def do_unlock(self,arg):
        """
        This unlocks the Door to the Space.
        USE WITH CAUTION!
        """
        unlock_door()
        print 'Door open. Exiting mdoshi. Enjoy your Stay!'
        return True

    def do_lock(self,arg):
        """
        This locks the Door to the Space.
        You normally would do this manually.
        Only use this if you know what you are doing!
        """
        lock_door()
        print 'Door locked. Exiting mdoshi. Have a nice Day!'
        return True

    def do_exit(self,arg):
        'Exit mdoshi'
        print 'Thank you for using mdoshi!'
        return True

    def do_open(self,arg):
        return self.do_unlock(arg)
        
    def do_close(self,arg):
        return self.do_lock(arg)

    def do_quit(self,arg):
        return self.do_exit(arg)

    def do_EOF(self,arg):
        return self.do_exit(arg)

    def print_topics(self, header, cmds, cmdlen, maxcol):
        """ Overwrite to hide undocumented functions """
        if header is not None:
            if cmds:
                self.stdout.write('%s\n'%str(header))
                if self.ruler:
                    self.stdout.write('%s\n'%str(self.ruler * len(header)))
                    self.columnize(cmds, maxcol-1)
                    self.stdout.write('\n')    
    
    def do_globalthermonuclearwar(self,arg):
        print 'GREETINGS PROFESSOR FALKEN'
        print ''
        print 'A STRANGE GAME.'
        print 'THE ONLY WINNING MOVE IS'
        print 'NOT TO PLAY.'
        print ''
        print 'HOW ABOUT A NICE GAME OF CHESS?'

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s',
                        filename='door.log',level=logging.INFO)
    # non interactive section
    if (len(sys.argv) > 2):
        if (sys.argv[1] == '-c'):
            if (sys.argv[2] == 'open') | (sys.argv[2] == 'unlock'):
                unlock_door()
                exit(0)
            elif (sys.argv[2] == 'close') | (sys.argv[2] == 'lock'):
                lock_door()
                exit(0)
            else:
                exit(1)
    # interactive section
    try:
        f = open('welcome','r')
        intro = f.read()
        f.close()
    except:
        intro = "Type ? or help for a list of commands"
    MDOSHI().cmdloop(intro)
