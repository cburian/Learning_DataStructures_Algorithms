"""
teacher solution modified
"""

from Chapter2_The_Queue.ch2_01_queue_class import Queue

import random


class PrintQueue(Queue):
    def __init__(self):
        super().__init__()


class Job:
    def __init__(self):
        self.pages = random.randint(1, 11)

    def print_page(self):
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self):
        if self.pages == 0:
            return True
        return False


class Printer:

    def __init__(self, print_queue):
        self.current_job = None
        self.print_queue = print_queue

    def get_job(self):
        try:
            self.current_job = self.print_queue.dequeue()
        except IndexError:
            print('No more Jobs to print')

    def print_job(self):
        self.get_job()

        if not self.current_job:
            return 'Can not print empty job!'

        while self.current_job.pages > 0:
            self.current_job.print_page()
            print(f'printing page: {self.current_job.pages}')

        if self.current_job.check_complete():
            return 'Print Complete!'
        else:
            return 'An error occurred!'


job1 = Job()
job2 = Job()
job3 = Job()
print('first job: ', job1)

print(f'\njob1 pages: {job1.pages}')
print(f'job2 pages: {job2.pages}')
print(f'job3 pages: {job3.pages}')

print_q = PrintQueue()
print_q.enqueue(job1)
print_q.enqueue(job2)
print_q.enqueue(job3)

print('\nlist of jobs in print_q: ')
print(print_q.items)

print('\npages in jobs: ')
for job in print_q.items:
    print(job.pages)

printer = Printer(print_q)
# printer.get_job()
print(printer.print_job())
print(printer.print_job())
print(printer.print_job())
print(printer.print_job())
