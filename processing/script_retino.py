"""
Script used to perform retinotopic analysis based on the IBC low-level visual
protocol.

Author: Bertrand Thirion, 2015--2017
"""
import os
import glob
from os.path import join as pjoin
import numpy as np
from nilearn.image import mean_img
from utils_retino import angular_maps, phase_maps
import nibabel as nib
from nilearn.plotting import plot_stat_map
import matplotlib.pyplot as plt
from nilearn.input_data import NiftiMasker



data_dir = '/neurospin/ibc/derivatives'

# find the subjects / sessions with the retinotopy protocol
cos_imgs = glob.glob(pjoin(data_dir, 'sub-*', 'ses-*', 'res_stats_*',
                           'z_score_maps', 'cos.nii.gz'))
subjects_sessions = []
for cos_img in cos_imgs:
    subject, session = cos_img.split('/')[-5:-3]
    subjects_sessions.append((subject + '_' +session))
subjects_sessions = np.unique(subjects_sessions)

# list all the acquisitions to take into account
acqs = ['res_stats_%s' % acq for acq in [
    'wedge_anti_pa', 'wedge_anti_ap', 'wedge_clock_ap', 'wedge_clock_pa',
    'exp_ring_pa', 'cont_ring_ap']]
THRESHOLD = 4. / np.sqrt(len(acqs))

for subject_session in subjects_sessions:
    subject, session = subject_session.split('_')
    work_dir = pjoin(data_dir, subject, session)
        # result directory 
    write_dir = pjoin(work_dir,  'retino_results')
    if not os.path.exists(write_dir):
        os.mkdir(write_dir)

    anat = pjoin(data_dir, subject, 'ses-00', 'anat', 'w%s_ses-00_T1w_nonan.nii.gz' % subject)

    # Compute the fixed effects across sessions
    # quick and dirty approach: sum z maps
    z_maps = [pjoin(work_dir, acq, 'z_score_maps', 'effects_interest.nii.gz')
              for acq in acqs]
    mean_z = mean_img(z_maps)

    plot_stat_map(mean_z, threshold=THRESHOLD, bg_img=anat, dim=0,
                  output_file=pjoin(write_dir, 'effects_of_interest.png'))
    mask = mean_z.get_data() > THRESHOLD
    mask_img = nib.Nifti1Image(mask.astype('uint8'), mean_z.affine)
    # to be completed with region size thresholding
    masker = NiftiMasker(mask_img=mask_img).fit()

    # take all images corresonding to sine regressors
    cos_wedge_clock = mean_img((
        pjoin(work_dir, 'res_stats_wedge_clock_pa', 'z_score_maps', 'cos.nii.gz'),
        pjoin(work_dir, 'res_stats_wedge_clock_ap', 'z_score_maps', 'cos.nii.gz')))

    sin_wedge_clock = mean_img((
        pjoin(work_dir, 'res_stats_wedge_clock_pa', 'z_score_maps', 'sin.nii.gz'),
        pjoin(work_dir, 'res_stats_wedge_clock_ap', 'z_score_maps', 'sin.nii.gz')))

    cos_wedge_anti = mean_img((
        pjoin(work_dir, 'res_stats_wedge_anti_pa', 'z_score_maps', 'cos.nii.gz'),
        pjoin(work_dir, 'res_stats_wedge_anti_ap', 'z_score_maps', 'cos.nii.gz')))

    sin_wedge_anti = mean_img((
        pjoin(work_dir, 'res_stats_wedge_anti_pa', 'z_score_maps', 'sin.nii.gz'),
        pjoin(work_dir, 'res_stats_wedge_anti_ap', 'z_score_maps', 'sin.nii.gz')))

    retino_imgs = {
        'cos_wedge_pos': cos_wedge_clock,
        'sin_wedge_pos': sin_wedge_clock,
        'sin_wedge_neg': cos_wedge_anti,
        'cos_wedge_neg': sin_wedge_anti,
        'cos_ring_pos': pjoin(
            work_dir, 'res_stats_exp_ring_pa', 'z_score_maps', 'cos.nii.gz'),
        'sin_ring_neg': pjoin(
            work_dir, 'res_stats_exp_ring_pa', 'z_score_maps', 'sin.nii.gz'),
        'sin_ring_pos': pjoin(
            work_dir, 'res_stats_cont_ring_ap', 'z_score_maps', 'sin.nii.gz'),
        'cos_ring_neg': pjoin(
            work_dir, 'res_stats_cont_ring_ap', 'z_score_maps', 'cos.nii.gz')
    }
    retino_coefs = {}
    for key in retino_imgs.keys():
        retino_coefs[key] = masker.transform(retino_imgs[key])
    
    phase_wedge, phase_ring, phase_hemo = phase_maps(
        retino_coefs, offset_ring=0, offset_wedge=0, do_wedge=True, do_ring=True, 
        do_phase_unwrapping=False, mesh=None, mask=mask_img)

    phase_wedge_img = masker.inverse_transform(phase_wedge)
    phase_ring_img = masker.inverse_transform(phase_ring)
    phase_hemo_img = masker.inverse_transform(phase_hemo)
    phase_wedge_img.to_filename(pjoin(write_dir, 'phase_wedge.nii.gz'))
    phase_ring_img.to_filename(pjoin(write_dir, 'phase_ring.nii.gz'))
    phase_hemo_img.to_filename(pjoin(write_dir, 'phase_hemo.nii.gz'))

    plot_stat_map(phase_wedge_img, title='polar angle',
                  bg_img=anat, dim=0, output_file=pjoin(write_dir, 'phase_wedge.png'))
    plot_stat_map(phase_ring_img, title='eccentricity',
                  bg_img=anat, dim=0, output_file=pjoin(write_dir, 'phase_ring.png'))
    plot_stat_map(phase_hemo_img, title='hemodynamics',
                  bg_img=anat, dim=0, output_file=pjoin(write_dir, 'phase_hemo.png'))

plt.show()
