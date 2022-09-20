import argparse
import partitura
import numpy as np

def main():
    # Arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--data_type',
                        help='data type: audio (yet to be supported) or symbolic (default: %(default)s',
                        type=str, default='symbolic')

    parser.add_argument('-f', '--music_input_format',
                        help='music format: MusicXML, MIDI (default: %(default)s',
                        type=str, default='MusicXML')

    parser.add_argument('-l', '--target_language', 
                        help = 'target language: Mandarin, Cantonese (default: %(default)s',
                        type=str, default='Mandarin')

    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()