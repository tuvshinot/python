""" context manager """
import contextlib


# Class based
class ClassBasedContextManager:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):  # exc_value is exception instance, exc_type is exception Class
        # cheap to import again cuz python caches
        import sys
        sys.stdout.write = self.original_write

        if exc_type is ZeroDivisionError:
            print('DO NOT divide by zero!')
            return True


with ClassBasedContextManager() as what:
    print(what)

# OR
manager = ClassBasedContextManager()
str_word = manager.__enter__()  # JABBERWOCKY
manager.__exit__(None, None, None)


# Generator as a coroutine using contextlib
@contextlib.contextmanager
def coroutine_based_context_manager():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''

    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'DO NOT DEVIDE by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


with coroutine_based_context_manager() as what:
    print(what)
