# DO NOT MODIFY THIS FILE DIRECTLY.  THIS FILE MUST BE CREATED BY
# mf6/utils/createpackages.py
# FILE created on August 15, 2024 07:36:53 UTC
from .. import mfpackage
from ..data.mfdatautil import ArrayTemplateGenerator


class ModflowRtmequ(mfpackage.MFPackage):
    """
    ModflowRtmequ defines a equ package within a rtm6 model.

    Parameters
    ----------
    model : MFModel
        Model that this package is a part of. Package is automatically
        added to model when it is initialized.
    loading_package : bool
        Do not set this parameter. It is intended for debugging and internal
        processing purposes only.
    export_array_ascii : boolean
        * export_array_ascii (boolean) keyword that specifies input griddata
          arrays should be written to layered ascii output files.
    sat_index : [double]
        * sat_index (double) saturation index.
    strt : [double]
        * strt (double) is the initial (starting) concentration of the phase---
          that is, concentration (mol/m3) at the beginning of the RTM Model
          simulation. One value is read for every model cell.
    filename : String
        File name for this package.
    pname : String
        Package name for this package.
    parent_file : MFPackage
        Parent package file that references this package. Only needed for
        utility packages (mfutl*). For example, mfutllaktab package must have 
        a mfgwflak package parent_file.

    """
    sat_index = ArrayTemplateGenerator(('rtm6', 'equ', 'griddata',
                                        'sat_index'))
    strt = ArrayTemplateGenerator(('rtm6', 'equ', 'griddata', 'strt'))
    package_abbr = "rtmequ"
    _package_type = "equ"
    dfn_file_name = "rtm-equ.dfn"

    dfn = [
           ["header", ],
           ["block options", "name export_array_ascii", "type keyword",
            "reader urword", "optional true", "mf6internal export_ascii"],
           ["block griddata", "name sat_index", "type double precision",
            "shape (nodes)", "reader readarray", "layered true",
            "default_value 0.0"],
           ["block griddata", "name strt", "type double precision",
            "shape (nodes)", "reader readarray", "layered true",
            "default_value 0.0"]]

    def __init__(self, model, loading_package=False, export_array_ascii=None,
                 sat_index=0.0, strt=0.0, filename=None, pname=None, **kwargs):
        super().__init__(model, "equ", filename, pname,
                         loading_package, **kwargs)

        # set up variables
        self.export_array_ascii = self.build_mfdata("export_array_ascii",
                                                    export_array_ascii)
        self.sat_index = self.build_mfdata("sat_index", sat_index)
        self.strt = self.build_mfdata("strt", strt)
        self._init_complete = True
