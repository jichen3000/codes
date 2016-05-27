import csv

def load(csv_filepath, skip_first=False, delimiter=','):
    with open(csv_filepath) as csv_file:
        reader = csv.reader(csv_file, delimiter=delimiter,)
        if skip_first:
            reader.next()
        return [row for row in reader]

def dump(content_list, csv_filepath, delimiter=","):
    with open(csv_filepath, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=delimiter)
        [writer.writerow(row) for row in content_list]
    return content_list

    

if __name__ == '__main__':
    from minitest import *

    read_filepath = 'read.csv'

    with test(csv.reader):
        with open(read_filepath) as csv_file:
            reader = csv.reader(csv_file, delimiter=',',)
            reader.next()
            rows = [row for row in reader]
            rows.must_equal([
                    ['1', '108.3', '246.7'],
                    ['2', '54.6', '137.2'],
                    ['3', '32.7', '99.3'],
                    ['4', '57.7', '154.5']])            
        pass

    with test(load):
        load(read_filepath).must_equal([
                ['1', '108.3', '246.7'],
                ['2', '54.6', '137.2'],
                ['3', '32.7', '99.3'],
                ['4', '57.7', '154.5']])
        load(read_filepath, False).must_equal([
                ['Id', 'Systole', 'Diastole'],
                ['1', '108.3', '246.7'],
                ['2', '54.6', '137.2'],
                ['3', '32.7', '99.3'],
                ['4', '57.7', '154.5']])

    with test(dump):
        content_list = [
                ['Id', 'Systole', 'Diastole'],
                ['1', '108.3', '246.7'],
                ['2', '54.6', '137.2'],
                ['3', '32.7', '99.3'],
                ['4', '57.7', '154.5']]
        dump(content_list, "write.csv")
