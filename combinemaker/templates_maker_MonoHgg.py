If you go to the end of this code you will find the following lines :

# actual main
if __name__ == "__main__":
    app = TemplatesApp()
    app.run()
    
 if __name__ == "__main__":   This means if this is the module being called then this part will work, if this module is being imported in some other module,
 then __name__ is not __main__ anymore, as in that case __name__ will be "templates_maker_MonoHgg" as we all know

Now, as we can see, app is an oject of class TemplatesApp, which is inherited from plotApp
Then, app.run()
Actually if you try to find out run() method, there is none in this module, but 
in the very first line you will find 
from diphotons.Utils.pyrapp import *

Now if you go to ../../../../Utils/python/pyrapp      
i.e. /afs/cern.ch/work/d/dbhowmik/public/Analysis/MHgg/2017Analysis/Fit_DiPhotonTools/CMSSW_9_4_9/src/diphotons/Utils/python/pyrapp

And look into pyrapp.py
Then you will find the method run(), which is the following 

   def run(self):
        self.__call__(self.options,self.args)
	if self.options.save:
            self.save()

which basically is calling the __call__() method of the class object

So, one should look into the __call__() method of the class TemplatesApp, which is the following :

    def __call__(self,options,args):
        """
        Main method. Called automatically by PyRoot class.
        """
        ## load ROOT style
        self.loadRootStyle()
        from ROOT import RooFit
        ROOT.gStyle.SetOptStat(111111)
	printLevel = ROOT.RooMsgService.instance().globalKillBelow()
        ROOT.RooMsgService.instance().setGlobalKillBelow(RooFit.FATAL)

	self.setup(options,args)

        if options.mix_templates:
            if options.verbose:
		print "calling mix templates"
            self.mixTemplates(options,args)

So the main two method to look into is :
setup() &
mixTemplates()

Need to look at "setu()" method and

mixTemplates() is again defined as :

    def mixTemplates(self,options,args):
        fout = self.openOut(options)
        ## fout.Print()
        fout.cd()
        self.doMixTemplates(options,args)
        self.saveWs(options,fout)

So, one should look into the "doMixTemplates()" method.
