"""
Create 3 classes that, together, model how a printer
could take print jobs out of a print queue.

Requirements:
1st class: PrintQueue - follows the queue data structure
                        implementation
2nd class: Job - pages attribute = random from 1 to 10
               - print_page() - decrements pages
               - check_complete() - checks if all pages
                                have been printed
3rd class: Printer - get_job() - makes use of the queue's
                            built-in dequeue method to take
                            the first job in the print queue
                            off of the queue.
                               - !account for the case where
                                  PrintQueue.items is empty
                   - print_job()
"""

from Chapter2_The_Queue.ch2_01_queue_class import Queue

from random import randint


class PrintQueue(Queue):
    def __init__(self):
        super().__init__()


class Job:
    def __init__(self):
        self.pages = randint(1, 10)
        self.print_q = PrintQueue()
        self.pages_left = self.print_q.size()

    def print_page(self):
        """
        Decrements pages
        """
        self.pages_left -= 1
        return self.print_q.dequeue()

    def check_complete(self):
        """
        Checks weather or not all pages have been printed
        """
        return self.print_q.is_empty()

    # def pages_left(self):
    #     """
    #     Returns the nr of pages left to print
    #     """
    #     return self.print_q.size()


class Printer:
    def __init__(self):
        self.job = Job()

    def get_job(self):
        """
        Makes use of the queue's built-in dequeue method to take
        the first job in the print queue off of the queue.

        ! Account for the case where PrintQueue.items is empty
        """
        if self.job.check_complete():
            return None
        return self.job.print_page()

    def print_job(self):
        return self.get_job()
