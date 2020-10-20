import nanny
import sys
# this module must be imported into the directory defined by site.USER_SITE


# check for existing exception hooks, and add ours to the chain
def attach_to_hook(our_hook):
    if sys.excepthook is not None:
        prev_except_hook = sys.excepthook
        def compound_except_hook(type_, val, tb):
            our_hook(type_, val, tb)
            prev_except_hook(type_, val, tb)

        sys.excepthook = compound_except_hook

    else:
        sys.excepthook = our_hook
 
attach_to_hook(nanny.nanny_exception_hook)
