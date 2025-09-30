# Provide mapping into reproin heuristic names
# Most of the information for mapping is taken from
# https://github.com/BIC-MNI/MNI_7T_DICOM_to_BIDS/tree/main?tab=readme-ov-file#mni-7t-dicom-to-bids-converter
# while operating on an example sequence ...
#
from heudiconv.heuristics import reproin

from heudiconv.heuristics.reproin import *

POPULATE_INTENDED_FOR_OPTS = {
    'matching_parameters': ['ImagingVolume', 'Shims'],
    'criterion': 'Closest'
}

directions_re = '(AP|PA|LR|RL|DV|VD)'

protocols2fix.update({
    '':  # for any study given.  Needs recent heudiconv
        [
            # All those come untested and correspond to some older pilot runs
            # regular expression, what to replace with
            #
            # Anatomicals
            (f'AAHead_Scout_.*', 'anat-scout'),
            (f'^anat-T1w_acq_mprage.*', r'anat-T1w_acq-mprage'),
            (f'^anat-angio_acq-tof_03mm_inplane', r'anat-angio'),
            # ex: anat-T1w_acq-mp2rage_0.7mm_CSptx
            # First to mape prefix
            (f'^anat-T1w_acq-mp2rage_0.7mm_CSptx', r'anat-MP2RAGE'),
            # and then I try to map suffix into inv etc
            # TODO: add to reproin!!! (I think)
            (f'^(anat-MP2RAGE)_INV([0-9])', r'\1_inv-\2'),
            # TODO: more suffixes if we manage above^^^
            # ex: anat-T2star_acq-me_gre_0.7iso_ASPIRE
            # TODO: if produces multiple nifti -- we might need to add heudiconv postprocessing
            (f'^anat-T2star_acq[-_]me_.*ASPIRE', r'anat-T2starw_acq-aspire'),
            #
            # Functionals
            # TODO: split mag|phase for 13,14-func-cross_acq-ep2d_MJC_19mm  https://github.com/nipy/heudiconv/issues/836
            (f'^func-cross_', r'func_task-rest_'),
            (f'^func-([a-z0-9]*)_.*', r'func_task-\1'),
            (f'_acq-ep2d_MJC_19mm', ''),
            #
            # Fieldmaps
            # ex: fmap-b1_tra_p2 -- 4 of those with no differences in series description
            (f'^fmap-b1_tra_p2', 'fmap-TB1TFL'),  # TODO: https://github.com/nipy/heudiconv/issues/835
            (f'^fmap-fmri_.*_dir-{directions_re}', r'fmap-epi_acq-fmri_dir-\1'),
            # ex: dwi_acq_multib_38dir_AP_acc9
            # ex: dwi_acq_multib_70dir_AP_acc9
            (f'^dwi_acq_multib_([0-9]+)dir_({directions_re})_acc[0-9]', r'dwi_acq-multib\1_dir-\2'),
            (f'^dwi_acq_b0_{directions_re}', r'dwi_acq-b0_dir-\1'),
            # TODO: do more from https://github.com/BIC-MNI/MNI_7T_DICOM_to_BIDS/
        ],
})

# We need to overload to be able to feed scans from varying
# accessions as for ses02 tasks being scanned in ses04.
# Fix to reproin sent in https://github.com/nipy/heudiconv/pull/508
#def fix_canceled_runs(seqinfo):
#    return seqinfo
# reproin.fix_canceled_runs = fix_canceled_runs
