#BEGIN_HEADER
#END_HEADER


class CatalogRepoTest:
    '''
    Module Name:
    CatalogRepoTest

    Module Description:
    
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass

    def run_test_1(self, ctx, params):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_test_1
        user = ctx['user_id']
        returnVal = {'params': params, 'user': user}
        #END run_test_1

        # At some point might do deeper type checking...
        if not isinstance(returnVal, object):
            raise ValueError('Method run_test_1 return value ' +
                             'returnVal is not type object as required.')
        # return the results
        return [returnVal]
