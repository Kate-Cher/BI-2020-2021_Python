import sys
import os.path


def length_filter(read, minimal):
    if len(read) >= int(minimal):
        return 1
    else:
        return 0


def gc_bounder(read, gc_min, gc_max):
    gc_count = (read.count('C') + read.count('G')) / (len(read) - 1) * 100
    if gc_min <= gc_count <= gc_max:
        return 1
    else:
        return 0


def arg_pars(arguments):
    keep_filtered = 0
    max_gc = 100.0
    min_gc = 0.0
    min_length = 0
    i = 1
    type_er_fl = 0
    prohib_symb = ['?', '/', ':', '*', '>', '<', '|', '+', '"', '\\', '--min_length', '--keep_filtered',
                   '--gc_bounds']
    error_state = False
    input_file = ''
    output_base_name = ''
    output_base_name_passed = ''
    output_base_name_failed = ''

    if len(arguments) == 1:
        print("No arguments found. Try -h/--help to help")
        error_state = True
    elif arguments[1] == '-h' or arguments[1] == '--help':
        print("This is fastq reads filtrator. \n"
              "Parameters you can use: \n"
              "\t --min_length:         Minimal length of read to keep (Optional argument)\n"
              "\t --keep_filtered:      Use this optional argument to save filtered reads \n"
              "\t --output_base_name:   Use this optional argument to set the base of the output filename \n"
              "\t\t\t\t'--output_base_name out_file' output files called out_file__passed.fastq (+ out_file__failed) \n"
              "\t --gc_bounds:          Use this optional arg to set GC content \n"
              "\t\t\t\t'--gc_bounds 55'     saves reads with GC content >= 55%\n"
              "\t\t\t\t'--gc_content 55 70' saves reads with GC content >=55% & <=70%\n"
              "fastq file is required positional argument\n\n"
              "Using example:\n"
              "\tpython filter_fastq.py --some_argument some_values test.fastq")
        error_state = True
    else:
        if arguments[len(arguments) - 1][-6:] == '.fastq':
            input_file = arguments[len(arguments) - 1]

            output_base_name = input_file[:-6]

            # Parsing arguments
            if os.path.isfile(input_file):

                while i < len(arguments):
                    if arguments[i] == "--min_length":
                        try:
                            min_length = int(arguments[i + 1])
                        except ValueError:
                            print("Minimal length should be integer except string found. Using default parameters")
                        i += 1
                    if arguments[i] == "--keep_filtered":
                        keep_filtered = 1
                    if arguments[i] == "--gc_bounds":
                        try:
                            min_gc = float(arguments[i + 1])
                        except ValueError:
                            type_er_fl = 1
                        try:
                            max_gc = float(arguments[i + 2])
                            i += 1
                        except ValueError:
                            pass
                        i += 1
                    if arguments[i] == "--output_base_name":
                        f = 1
                        for symb in prohib_symb:
                            if symb in arguments[i + 1]:
                                f = 0
                        if f == 1:
                            output_base_name = arguments[i + 1]
                            i += 1
                        else:
                            print("Wrong base name. Using default value \n"
                                  f"Prohibited symbols: ")
                            print(*prohib_symb)
                            print('Using default base')
                    i += 1

                output_base_name_passed = output_base_name + "__passed.fastq"
                output_base_name_failed = output_base_name + "__failed.fastq"

                # Run information module. Checking argument correctness

                print('Run information: ')
                print(f"\tPassed reads are in {output_base_name_passed}")
                if keep_filtered == 1:
                    print(f"\tFailed reads are in {output_base_name_failed}")
                else:
                    print('\tReads that have not passed the filter are not saved')
                print(f"Passed reads: \n"
                      f"\t Minimal read's length: {min_length}")
                if type_er_fl == 1:
                    print("Error in GC content type. Must be float. Using default values")
                else:
                    if max_gc < min_gc <= 100:
                        print('Minimal GC content must be first. Changing positions')
                        min_gc, max_gc = max_gc, min_gc
                    if max_gc > 100:
                        print('There were error in maximal GC content (> 100%). Using default value')
                        max_gc = 100
                    if min_gc >= 100:
                        print('There were error in minimal GC content (> 100%). Using default value')
                        min_gc = 0
                print(f"\t Minimal read's gc content: {min_gc} \n"
                      f"\t Maximal read's gc content: {max_gc}\n")

            else:
                error_state = True
                print('No such file in directory')
        else:
            error_state = True
            print("There is no fastq file. Check file name correctness and try again. \n"
                  "Fastq file is required last positional argument")

    arg_dict = {
        "keep_filtered": keep_filtered,
        "max_gc": max_gc,
        "min_gc": min_gc,
        "min_length": min_length,
        "type_er_fl": type_er_fl,
        "error_state": error_state,
        "output_base_name": output_base_name,
        "input_file": input_file,
        "output_base_name_passed": output_base_name_passed,
        "output_base_name_failed": output_base_name_failed
    }
    return arg_dict


def filter_reads(arg_dict):
    if not arg_dict["error_state"]:
        passed_counter = 0
        failed_counter = 0
        with open(arg_dict["input_file"]) as fastq:
            with open(arg_dict["output_base_name_passed"], 'w') as output_passed:
                with open(arg_dict["output_base_name_failed"], 'w') as output_failed:
                    for line in fastq:
                        lines = [line]
                        for i in range(3):
                            lines.append(fastq.readline())
                        if length_filter(lines[1], arg_dict["min_length"]) * gc_bounder(lines[1], arg_dict["min_gc"],
                                                                                        arg_dict["max_gc"]) == 1:
                            output_passed.writelines(lines)
                            passed_counter += 1
                        else:
                            failed_counter += 1
                            if arg_dict["keep_filtered"] == 1:
                                output_failed.writelines(lines)

        all_reads = passed_counter + failed_counter
        print(f"Number of passed filtration reads: {passed_counter}")
        print("Percent of passed filtration reads: %.4f" % (passed_counter / all_reads * 100), "%")
        print(f"\nNumber of failed filtration reads: {failed_counter}")
        print("Percent of failed filtration reads: %.4f" % (failed_counter / all_reads * 100), "%")


arg = sys.argv
parsed_arg = arg_pars(arg)
if not parsed_arg["error_state"]:
    filter_reads(parsed_arg)
