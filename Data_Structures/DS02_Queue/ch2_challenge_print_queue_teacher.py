"""
teacher solution
"""

import random


class PrintQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None

    def is_empty(self):
        return self.items == []


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

    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:
            return 'No more Jobs to print'

    def print_job(self, job):

        while job.pages > 0:
            job.print_page()

        if job.check_complete():
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

printer = Printer()
printer.get_job(print_q)
print(printer.print_job(job1))
print(printer.print_job(job2))
print(printer.print_job(job3))
