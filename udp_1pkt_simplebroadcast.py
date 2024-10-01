class STLS1(object):

    def create_stream (self):
        return STLStream( 
            packet = 
                    STLPktBuilder(
                        pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src="16.0.0.1",dst="48.0.0.1")/
                                UDP(dport=12,sport=1025)/(8958*'x')
                    ),
             mode = STLTXCont())

    def get_streams (self, tunables, **kwargs):
        parser = argparse.ArgumentParser(description='Argparser for {}'.format(os.path.basename(_file_)), 
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        args = parser.parse_args(tunables)
        # create 1 stream 
        return [ self.create_stream() ]


# dynamic load - used for trex console or simulator
def register():
    return STLS1()
