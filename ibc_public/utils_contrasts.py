""" This modules specifies contrasts for the IBC tasks

Author: Bertrand Thirion, Ana Luisa Pinho 2014--2020
"""

import numpy as np


def make_contrasts(paradigm_id, design_matrix_columns=None):
    """ return the contrasts matching a string"""
    if paradigm_id == 'archi_standard':
        return archi_standard(design_matrix_columns)
    elif paradigm_id == 'archi_social':
        return archi_social(design_matrix_columns)
    elif paradigm_id == 'archi_spatial':
        return archi_spatial(design_matrix_columns)
    elif paradigm_id == 'archi_emotional':
        return archi_emotional(design_matrix_columns)
    elif paradigm_id == 'hcp_emotion':
        return hcp_emotion(design_matrix_columns)
    elif paradigm_id == 'hcp_gambling':
        return hcp_gambling(design_matrix_columns)
    elif paradigm_id == 'hcp_language':
        return hcp_language(design_matrix_columns)
    elif paradigm_id == 'hcp_motor':
        return hcp_motor(design_matrix_columns)
    elif paradigm_id == 'hcp_wm':
        return hcp_wm(design_matrix_columns)
    elif paradigm_id == 'hcp_relational':
        return hcp_relational(design_matrix_columns)
    elif paradigm_id == 'hcp_social':
        return hcp_social(design_matrix_columns)
    elif paradigm_id == 'language':
        return rsvp_language(design_matrix_columns)
    elif paradigm_id == 'colour':
        return colour(design_matrix_columns)
    elif paradigm_id in ['cont_ring', 'exp_ring', 'wedge_clock', ###
                         'wedge_anti', 'wedge', 'ring']:###
        return retino(design_matrix_columns)###
    elif paradigm_id in ['wedge', 'wedge_anti', 'wedge_clock']:
        return wedge(design_matrix_columns)
    elif paradigm_id in ['ring', 'cont_ring', 'exp_ring']:
        return ring(design_matrix_columns)
    elif paradigm_id[:10] == 'preference':
        domain = paradigm_id[11:]
        if domain[-1] == 's':
            domain = domain[: -1]
        return preferences(design_matrix_columns, domain)
    elif paradigm_id == 'MTTWE':
        return mtt_we_relative(design_matrix_columns)
    elif paradigm_id == 'MTTNS':
        return mtt_sn_relative(design_matrix_columns)
    elif paradigm_id == 'emotional_pain':
        return emotional_pain(design_matrix_columns)
    elif paradigm_id == 'pain_movie':
        return pain_movie(design_matrix_columns)
    elif paradigm_id == 'theory_of_mind':
        return theory_of_mind(design_matrix_columns)
    elif paradigm_id == 'VSTM':
        return vstm(design_matrix_columns)
    elif paradigm_id == 'enumeration':
        return enumeration(design_matrix_columns)
    elif paradigm_id == 'clips_trn':
        return dict([])
    elif paradigm_id == 'self':
        return self_localizer(design_matrix_columns)
    elif paradigm_id == 'lyon_moto':
        return lyon_moto(design_matrix_columns)
    elif paradigm_id == 'lyon_mcse':
        return lyon_mcse(design_matrix_columns)
    elif paradigm_id == 'lyon_mveb':
        return lyon_mveb(design_matrix_columns)
    elif paradigm_id == 'lyon_mvis':
        return lyon_mvis(design_matrix_columns)
    elif paradigm_id == 'lyon_lec1':
        return lyon_lec1(design_matrix_columns)
    elif paradigm_id == 'lyon_lec2':
        return lyon_lec2(design_matrix_columns)
    elif paradigm_id == 'lyon_audi':
        return lyon_audi(design_matrix_columns)
    elif paradigm_id == 'lyon_visu':
        return lyon_visu(design_matrix_columns)
    elif paradigm_id == 'audio':
        return audio(design_matrix_columns)
    elif paradigm_id == 'bang':
        return bang(design_matrix_columns)
    elif paradigm_id == 'selective_stop_signal':
        return selective_stop_signal(design_matrix_columns)
    elif paradigm_id == 'stop_signal':
        return stop_signal(design_matrix_columns)
    elif paradigm_id == 'stroop':
        return stroop(design_matrix_columns)
    elif paradigm_id == 'discount':
        return discount(design_matrix_columns)
    elif paradigm_id == 'attention':
        return attention(design_matrix_columns)
    elif paradigm_id == 'ward_and_aliport':
        return towertask(design_matrix_columns)
    elif paradigm_id == 'two_by_two':
        return two_by_two(design_matrix_columns)
    elif paradigm_id == 'columbia_cards':
        return columbia_cards(design_matrix_columns)
    elif paradigm_id == 'dot_patterns':
        return dot_patterns(design_matrix_columns)
    elif paradigm_id == 'biological_motion1':
        return biological_motion1(design_matrix_columns)
    elif paradigm_id == 'biological_motion2':
        return biological_motion2(design_matrix_columns)
    elif paradigm_id == 'mathlang':
        return math_language(design_matrix_columns)
    elif paradigm_id == 'spatial_navigation':
        return spatial_navigation(design_matrix_columns)
    elif paradigm_id == 'EmoMem':
        return emotional_memory(design_matrix_columns)
    elif paradigm_id == 'EmoReco':
        return emotion_recognition(design_matrix_columns)
    elif paradigm_id == 'StopNogo':
        return stop_nogo(design_matrix_columns)
    elif paradigm_id == 'Catell':
        return oddball(design_matrix_columns)
    elif paradigm_id == 'VSTMC':
        return vstmc(design_matrix_columns)
    elif paradigm_id == 'FingerTapping':
        return finger_tapping(design_matrix_columns)
    elif paradigm_id == 'RewProc':
        return reward_processing(design_matrix_columns)
    elif paradigm_id == 'NARPS':
        return narps(design_matrix_columns)
    elif paradigm_id == 'FaceBody':
        return face_body(design_matrix_columns)
    elif paradigm_id == 'Scene':
        return scenes(design_matrix_columns)
    else:
        raise ValueError('%s Unknown paradigm' % paradigm_id)


def _elementary_contrasts(design_matrix_columns):
    """Returns a dictionary of contrasts for all columns
        of the design matrix"""
    con = {}
    n_columns = len(design_matrix_columns)
    # simple contrasts
    for i in range(n_columns):
        con[design_matrix_columns[i]] = np.eye(n_columns)[i]
    return con


def _append_effects_interest_contrast(design_matrix_columns, contrast):
    """appends a contrast for all derivatives"""
    n_columns = len(design_matrix_columns)
    # simple contrasts
    con = []
    nuisance = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'constant'] +\
               ['drift_%d' % i for i in range(20)] +\
               ['conf_%d' % i for i in range(20)]
    for i in range(n_columns):
        if design_matrix_columns[i] in nuisance:
            continue
        if len(design_matrix_columns[i]) > 11:
            if design_matrix_columns[i][-11:] == '_derivative':
                continue
        con.append(np.eye(n_columns)[i])
    if con != []:
        contrast['effects_interest'] = np.array(con)
    return contrast


def _append_derivative_contrast(design_matrix_columns, contrast):
    """appends a contrast for all derivatives"""
    n_columns = len(design_matrix_columns)
    # simple contrasts
    con = []
    for i in range(n_columns):
        if len(design_matrix_columns[i]) > 11:
            if design_matrix_columns[i][-11:] == '_derivative':
                con.append(np.eye(n_columns)[i])

    if con != []:
        contrast['derivatives'] = np.array(con)
    return contrast


def narps(design_matrix_columns):
    """ Contrasts for reward processing experiment"""
    contrast_names = ['gain', 'loss', 'weakly_accept', 'weakly_reject',
                      'strongly_accept', 'strongly_reject',
                      'reject-accept', 'accept-reject']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names[:6]])
    contrasts['reject-accept'] = con['weakly_reject'] + con['strongly_reject']\
        - con['weakly_accept'] - con['strongly_accept']
    contrasts['accept-reject'] = - contrasts['reject-accept']
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def scenes(design_matrix_columns):
    """Contrasts for scenes protocol"""
    contrast_names = [
        'dot_easy_left', 'dot_easy_right', 'dot_hard_left', 'dot_hard_right',
        'scene_impossible_correct', 'scene_impossible_incorrect',
        'scene_possible_correct', 'scene_possible_incorrect',
        'scene_possible_correct-scene_impossible_correct',
        'scene_correct-dot_correct',
        'dot_left-right',
        'dot_hard-easy'
        ]
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names[:8]])
    contrasts['scene_possible_correct-scene_impossible_correct'] =\
        con['scene_possible_correct'] - con['scene_impossible_correct']
    contrasts['scene_correct-dot_correct'] =\
        con['scene_impossible_correct'] + con['scene_possible_correct'] -\
        con['scene_impossible_incorrect'] - con['scene_possible_incorrect']
    contrasts['dot_left-right'] =\
        con['dot_easy_left'] + con['dot_hard_left'] -\
        con['dot_easy_right'] - con['dot_hard_right']
    contrasts['dot_hard-easy'] =\
        -con['dot_easy_left'] + con['dot_hard_left'] -\
        con['dot_easy_right'] + con['dot_hard_right']
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def face_body(design_matrix_columns):
    """ Contrasts for FaceBody task"""
    contrast_names = [
        'bodies_body', 'bodies_limb',
        'characters_number', 'characters_word',
        'faces_adult', 'faces_child',
        'objects_car', 'objects_instrument',
        'places_corridor', 'places_house',
        'bodies-others', 'characters-others', 'faces-others',
        'objects-others', 'places-others']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names[:10]])
    mean_ = np.sum(list(contrasts.values()), 0)
    bodies = con['bodies_body'] + con['bodies_limb']
    characters = con['characters_number'] + con['characters_word']
    faces = con['faces_adult'] + con['faces_child']
    objects = con['objects_car'] + con['objects_instrument']
    places = con['places_corridor'] + con['places_house']
    contrasts['bodies-others'] = 5 * bodies - mean_
    contrasts['characters-others'] = 5 * characters - mean_
    contrasts['faces-others'] = 5 * faces - mean_
    contrasts['objects-others'] = 5 * objects - mean_
    contrasts['places-others'] = 5 * places - mean_
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def reward_processing(design_matrix_columns):
    """ Contrasts for reward processing experiment"""
    contrast_names = [
        'stim', 'out_-20', 'out_+20', 'out_-10', 'out_+10',
        'green-purple', 'purple-green', 'left-right', 'right-left',
        'switch', 'stay', 'switch-stay', 'stay-switch']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names[:5]])
    contrasts['green-purple'] = con['green']
    contrasts['purple-green'] = - con['green']
    contrasts['left-right'] = con['left']
    contrasts['right-left'] = - con['left']
    contrasts['switch'] = con['switch']
    contrasts['stay'] = con['stay']
    contrasts['switch-stay'] = con['switch'] - con['stay']
    contrasts['stay-switch'] = con['stay'] - con['switch']
    """
    contrast_names = [
        'out_+10', 'out_+20', 'out_-10', 'out_-20', 'stim',
        'resp_green-left_switch', 'resp_green-right_init',
        'resp_green-right_stay', 'resp_green-right_switch',
        'resp_purple-left_stay', 'resp_purple-left_switch',
        'resp_purple-right_stay', 'resp_purple-right_switch',
        'gain-loss', 'loss-gain', 'stay-switch', 'switch-stay',
        # 'gain-loss_stay', 'loss-gain_stay',
        # 'gain-loss_switch', 'loss-gain_switch',
        'green-purple', 'purple-green',
        'left-right', 'right-left']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names[:13]])
    stay = con['resp_green-right_stay'] + con['resp_purple-left_stay']\
        + con['resp_purple-right_stay']
    switch = con['resp_green-left_switch'] + con['resp_green-right_switch']\
        + con['resp_purple-left_switch'] + con['resp_purple-right_switch']
    contrasts['stay-switch'] = stay - switch
    contrasts['switch-stay'] = switch - stay
    contrasts['gain-loss'] = con['out_+10'] + con['out_+20']\
        - con['out_-10'] - con['out_-20']
    contrasts['loss-gain'] = - contrasts['gain-loss']
    green = con['resp_green-left_switch'] + con['resp_green-right_init']\
        + con['resp_green-right_stay'] + con['resp_green-right_switch']
    purple = con['resp_purple-left_stay'] + con['resp_purple-left_switch']\
        + con['resp_purple-right_stay'] + con['resp_purple-right_switch']
    left = con['resp_green-left_switch'] + con['resp_purple-left_stay']\
        + con['resp_purple-left_switch']
    right = con['resp_green-right_stay'] + con['resp_green-right_switch']\
        + con['resp_purple-right_stay'] + con['resp_purple-right_switch']
    contrasts['green-purple'] = green - purple
    contrasts['purple-green'] = - contrasts['green-purple']
    contrasts['left-right'] = left - right
    contrasts['right-left'] = - contrasts['left-right']
    """
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def math_language(design_matrix_columns):
    """ Contrasts for math-language task"""
    contrast_names = [
        'colorlessg_auditory', 'colorlessg_visual',
        'wordlist_auditory', 'wordlist_visual',
        'arithmetic_fact_auditory', 'arithmetic_fact_visual',
        'arithmetic_principle_auditory', 'arithmetic_principle_visual',
        'theory_of_mind_auditory', 'theory_of_mind_visual',
        'geometry_fact_auditory', 'geometry_fact_visual',
        'general_auditory', 'general_visual',
        'context_auditory', 'context_visual',
        'visual-auditory', 'auditory-visual',
        'colorlessg-wordlist',
        'general-colorlessg',
        'math-nonmath', 'nonmath-math',
        'geometry-othermath',
        'arithmetic_principle-othermath',
        'arithmetic_fact-othermath',
        'theory_of_mind-general', 'context-general', 'theory_of_mind-context',
        'context-theory_of_mind',
        'theory_of_mind_and_context-general']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names[:16]])
    contrasts['auditory-visual'] =\
        np.sum([con[name] for name in contrast_names[:16:2]], 0) -\
        np.sum([con[name] for name in contrast_names[1:16:2]], 0)
    contrasts['visual-auditory'] = - contrasts['auditory-visual']
    contrasts['colorlessg-wordlist'] =\
        con['colorlessg_auditory'] + con['colorlessg_visual'] - (
        con['wordlist_auditory'] + con['wordlist_visual'])
    contrasts['general-colorlessg'] =\
        con['general_auditory'] + con['general_visual'] -\
        (con['colorlessg_auditory'] + con['colorlessg_visual'])
    contrasts['math-nonmath'] = (
        con['arithmetic_fact_auditory'] + con['arithmetic_fact_visual'] +
        con['arithmetic_principle_auditory'] +
        con['arithmetic_principle_visual'] +
        con['geometry_fact_auditory'] + con['geometry_fact_visual']) - (
        con['theory_of_mind_auditory'] + con['theory_of_mind_visual'] +
        con['context_auditory'] + con['context_visual'] +
        con['general_auditory'] + con['general_visual'])
    contrasts['nonmath-math'] = - contrasts['math-nonmath']
    contrasts['geometry-othermath'] =\
        con['geometry_fact_auditory'] + con['geometry_fact_visual'] - 0.5 * (
        con['arithmetic_fact_auditory'] + con['arithmetic_fact_visual'] +
        con['arithmetic_principle_auditory'] +
        con['arithmetic_principle_visual'])
    contrasts['arithmetic_principle-othermath'] =\
        con['arithmetic_principle_auditory'] +\
        con['arithmetic_principle_visual'] - 0.5 * (
        con['arithmetic_fact_auditory'] + con['arithmetic_fact_visual'] +
        con['geometry_fact_auditory'] + con['geometry_fact_visual'])
    contrasts['arithmetic_fact-othermath'] =\
        con['arithmetic_fact_auditory'] + con['arithmetic_fact_visual'] -\
        0.5 * (
        con['geometry_fact_auditory'] + con['geometry_fact_visual'] +
        con['arithmetic_principle_auditory'] +
        con['arithmetic_principle_visual'])
    contrasts['theory_of_mind-general'] =\
        con['theory_of_mind_auditory'] + con['theory_of_mind_visual'] - (
        con['general_auditory'] + con['general_visual'])
    contrasts['context-general'] =\
        con['context_auditory'] + con['context_visual'] - (
        con['general_auditory'] + con['general_visual'])
    contrasts['theory_of_mind-context'] =\
        con['theory_of_mind_auditory'] + con['theory_of_mind_visual'] - (
        con['context_auditory'] + con['context_visual'])
    contrasts['context-theory_of_mind'] = - contrasts['theory_of_mind-context']
    contrasts['theory_of_mind_and_context-general'] = .5 * (
        con['theory_of_mind_auditory'] + con['theory_of_mind_visual'] +
        con['context_auditory'] + con['context_visual']) - (
        con['general_auditory'] + con['general_visual'])
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def spatial_navigation(design_matrix_columns):
    """ Contrasts for spatial navigation task"""
    contrast_names = [
        'experimental-intersection', 'experimental-control', 'encoding_phase',
        'intersection', 'retrieval', 'control', 'pointing_control',
        'experimental', 'pointing_experimental', 'navigation']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)

    contrasts = {'encoding_phase': con['encoding_phase'],
                 'navigation': con['navigation'],
                 'experimental': con['experimental'],
                 'pointing_experimental': con['pointing_experimental'],
                 'control': con['control'],
                 'pointing_control': con['pointing_control'],
                 'intersection': con['intersection'],
                 'experimental-control': con['experimental'] - con['control'],
                 'retrieval':
                     con['experimental'] + con['pointing_experimental'] -
                     con['control'] - con['pointing_control'],
                 'experimental-intersection':
                     con['experimental'] - con['intersection']
                 }

    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def wedge(design_matrix_columns):
    """ Contrasts for wedge stim"""
    contrast_names = [
        'lower_meridian', 'lower_right', 'right_meridian', 'upper_right',
        'upper_meridian', 'upper_left', 'left_meridian', 'lower_left',
    ]
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names])
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def ring(design_matrix_columns):
    """ Contrasts for ring stim"""
    contrast_names = ['foveal', 'middle', 'peripheral']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names])
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def emotional_memory(design_matrix_columns):
    """ Contrasts for emotional memory protocol"""
    contrast_names = ['neutral_image', 'negative_image', 'positive_image', 'object',
                      'positive-neutral_image', 'negative-neutral_image']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names[:4]])
    contrasts['positive-neutral_image'] = contrasts['positive_image'] - contrasts['neutral_image']
    contrasts['negative-neutral_image'] = contrasts['negative_image'] - contrasts['neutral_image']
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def emotion_recognition(design_matrix_columns):
    """ Contrasts for emotion recognition protocol"""
    contrast_names = [
        'neutral_male', 'angry_male', 'neutral_female', 'angry_female',
        'neutral', 'angry', 'angry-neutral', 'neutral-angry', 'male-female',
        'female-male']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'neutral_male': con['neutral_male'],
        'angry_male': con['angry_male'],
        'neutral_female': con['neutral_female'],
        'angry_female': con['angry_female'],
        'neutral': con['neutral_male'] + con['neutral_female'],
        'angry': con['angry_male'] + con['angry_female'],
        }
    contrasts['angry-neutral'] = contrasts['angry'] - contrasts['neutral']
    contrasts['neutral-angry'] = - contrasts['angry-neutral']
    contrasts['male-female'] = (
        con['neutral_male'] + con['angry_male'] - con['neutral_female']
        - con['angry_female'])
    contrasts['female-male'] = - contrasts['male-female']
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def oddball(design_matrix_columns):
    """ Contrasts for oddball protocol"""
    contrast_names = ['easy', 'hard', 'hard-easy']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'easy': con['easy'],
        'hard': con['hard'],
        'hard-easy': con['hard'] - con['easy'],}
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def stop_nogo(design_matrix_columns):
    """ Contrasts for stop nogo protocol"""
    contrast_names = ['go', 'nogo', 'successful_stop', 'unsuccessful_stop',
                      'nogo-go', 'unsuccessful-successful_stop',
                      'successful+nogo-unsuccessful']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'go': con['go'],
        'nogo': con['nogo'],
        'successful_stop': con['successful_stop'],
        'unsuccessful_stop': con['unsuccessful_stop'],
        'nogo-go': con['nogo'] - con['go'],
        'unsuccessful-successful_stop': con['unsuccessful_stop'] - con['successful_stop'],
        'successful+nogo-unsuccessful': con['successful_stop'] + con['nogo'] -  con['unsuccessful_stop']
    }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def finger_tapping(design_matrix_columns):
    """ Contrasts for oddball protocol"""
    contrast_names = ['specified', 'chosen', 'null',
                      'chosen-specified', 'specified-null', 'chosen-null']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'specified': con['specified'],
        'chosen': con['chosen'],
        'null': con['null'],
        'chosen-specified': con['chosen'] - con['specified'],
        'specified-null': con['specified'] - con['null'],
        'chosen-null': con['chosen'] - con['null']}
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def vstmc(design_matrix_columns):
    """ Contrasts for vstmc protocol"""
    contrast_names = ['stim_load1', 'stim_load2', 'stim_load3',
                      'resp_load1', 'resp_load2', 'resp_load3',
                      'stim', 'resp', 'stim_load3-load1',
                      'resp_load3-load1'
    ]
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'stim_load1': con['stim_load1'],
        'stim_load2': con['stim_load2'],
        'stim_load3': con['stim_load3'],
        'resp_load1': con['resp_load1'],
        'resp_load2': con['resp_load2'],
        'resp_load3': con['resp_load3'],
        'stim': con['stim_load1'] + con['stim_load2'] + con['stim_load3'],
        'resp': con['resp_load1'] + con['resp_load2'] + con['resp_load3'],
        'stim_load3-load1': con['stim_load3'] - con['stim_load1'],
        'resp_load3-load1': con['resp_load3'] - con['resp_load1'],
    }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts



def biological_motion1(design_matrix_columns):
    """ Contrasts for biological motion 1 protocol"""
    contrast_names = ['global_upright', 'global_inverted',
                      'natural_upright', 'natural_inverted',
                      'global_upright - natural_upright',
                      'global_upright - global_inverted',
                      'natural_upright - natural_inverted',
                      ]
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names[:4]])
    contrasts['global_upright - natural_upright'] =\
        contrasts['global_upright'] - contrasts['natural_upright']
    contrasts['global_upright - global_inverted'] = \
        contrasts['global_upright'] - contrasts['global_inverted']
    contrasts['natural_upright - natural_inverted'] =\
        contrasts['natural_upright'] - contrasts['natural_inverted']
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def biological_motion2(design_matrix_columns):
    """ Contrasts for biological motion 1 protocol"""
    contrast_names = ['modified_upright', 'modified_inverted',
                      'natural_upright', 'natural_inverted',
                      'natural_upright - modified_upright',
                      'modified_upright - modified_inverted',
                      'natural_upright - natural_inverted',
                      ]
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names[:4]])
    contrasts['natural_upright - modified_upright'] =\
        contrasts['natural_upright'] - contrasts['modified_upright']
    contrasts['modified_upright - modified_inverted'] = \
        contrasts['modified_upright'] - contrasts['modified_inverted']
    contrasts['natural_upright - natural_inverted'] =\
        contrasts['natural_upright'] - contrasts['natural_inverted']
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def dot_patterns(design_matrix_columns):
    """ Contrasts for Stanford's dot patterns protocol"""
    contrast_names = [
        'cue',
        'correct_cue_correct_probe',
        'correct_cue_incorrect_probe',
        'incorrect_cue_correct_probe',
        'incorrect_cue_incorrect_probe',
        'correct_cue_incorrect_probe-correct_cue_correct_probe',
        'incorrect_cue_incorrect_probe-incorrect_cue_correct_probe',
        'correct_cue_incorrect_probe-incorrect_cue_correct_probe',
        'incorrect_cue_incorrect_probe-correct_cue_incorrect_probe',
        'correct_cue-incorrect_cue',
        'incorrect_probe-correct_probe'
    ]
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'cue': con['cue'],
        'correct_cue_correct_probe': con['correct_cue_correct_probe'],
        'correct_cue_incorrect_probe': con['correct_cue_incorrect_probe'],
        'incorrect_cue_correct_probe': con['incorrect_cue_correct_probe'],
        'incorrect_cue_incorrect_probe': con['incorrect_cue_incorrect_probe'],
        'correct_cue_incorrect_probe-correct_cue_correct_probe':
            con['correct_cue_incorrect_probe'] -
            con['correct_cue_correct_probe'],
        'incorrect_cue_incorrect_probe-incorrect_cue_correct_probe':
            con['incorrect_cue_incorrect_probe'] -
            con['incorrect_cue_correct_probe'],
        'correct_cue_incorrect_probe-incorrect_cue_correct_probe':
            con['correct_cue_incorrect_probe'] -
            con['incorrect_cue_correct_probe'],
        'incorrect_cue_incorrect_probe-correct_cue_incorrect_probe':
            con['incorrect_cue_incorrect_probe'] -
            con['correct_cue_incorrect_probe'],
        'correct_cue-incorrect_cue':
            con['correct_cue_correct_probe']
            + con['correct_cue_incorrect_probe']
            - con['incorrect_cue_correct_probe']
            - con['incorrect_cue_incorrect_probe'],
        'incorrect_probe-correct_probe':
            - con['correct_cue_correct_probe']
            + con['correct_cue_incorrect_probe']
            - con['incorrect_cue_correct_probe']
            + con['incorrect_cue_incorrect_probe'],
    }

    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def columbia_cards(design_matrix_columns):
    """ Contrasts for Stanford's Columbia Cards protocol"""
    contrast_names = ['num_loss_cards', 'loss', 'gain']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names])
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def discount(design_matrix_columns):
    """ Contrasts for Stanford's discount protocol"""
    contrast_names = ['delay', 'amount']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names])
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def towertask(design_matrix_columns):
    """ Contrasts for Stanford's Tower task protocol"""
    contrast_names = ['planning_ambiguous_intermediate',
                      'planning_ambiguous_direct',
                      'planning_unambiguous_intermediate',
                      'planning_unambiguous_direct',
                      'move_ambiguous_intermediate',
                      'move_ambiguous_direct',
                      'move_unambiguous_intermediate',
                      'move_unambiguous_direct',
                      'intermediate-direct',
                      'ambiguous-unambiguous']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(cn, con[cn]) for cn in contrast_names[:-2]])
    contrasts['intermediate-direct'] =\
        con['planning_ambiguous_intermediate']\
        + con['planning_unambiguous_intermediate']\
        - (con['planning_ambiguous_direct']
           + con['planning_unambiguous_direct'])
    contrasts['ambiguous-unambiguous'] =\
        con['planning_ambiguous_intermediate']\
        - con['planning_unambiguous_intermediate'] +\
        con['planning_ambiguous_direct']\
        - con['planning_unambiguous_direct']
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def two_by_two(design_matrix_columns):
    """ Contrasts for Stanford's two-bytwo task protocol"""
    contrast_names = [
        'cue_taskstay_cuestay',
        'cue_taskstay_cueswitch',
        'cue_taskswitch_cuestay',
        'cue_taskswitch_cueswitch',
        'stim_taskstay_cuestay',
        'stim_taskstay_cueswitch',
        'stim_taskswitch_cuestay',
        'stim_taskswitch_cueswitch',
        'task_swtich-stay',
        'cue_switch']
    #  'task_stay_cue_stay', 'task_switch_cue_switch',
    #  'task_switch_cue_stay', 'task_stay_cue_switch',
    #  'task_switch-stay', 'cue_switch']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(cn, con[cn]) for cn in contrast_names[:-2]])
    contrasts['task_swtich-stay'] =\
        con['cue_taskswitch_cueswitch'] + con['cue_taskswitch_cuestay']\
        - con['cue_taskstay_cueswitch'] - con['cue_taskstay_cuestay']
    contrasts['cue_switch'] = con['cue_taskstay_cueswitch']\
        - con['cue_taskstay_cuestay']

    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def attention(design_matrix_columns):
    """ Contrasts for Stanford's attention protocol"""
    contrast_names = [
        'spatial_cue-double_cue',
        'spatial_cue', 'double_cue',
        'incongruent-congruent', 'spatial_incongruent-spatial_congruent',
        'double_incongruent-double_congruent', 'spatial_incongruent',
        'double_congruent', 'spatial_congruent',
        'double_incongruent'
        ]
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'spatial_cue-double_cue': con['spatialcue'] - con['doublecue'],
        'spatial_cue': con['spatialcue'],
        'double_cue': con['doublecue'],
        'incongruent-congruent':
            con['spatial_incongruent'] - con['spatial_congruent'] +
            con['double_incongruent'] - con['double_congruent'],
        'spatial_incongruent-spatial_congruent':
            con['spatial_incongruent'] - con['spatial_congruent'],
        'double_incongruent-double_congruent':
            con['double_incongruent'] - con['double_congruent'],
        'spatial_incongruent': con['spatial_incongruent'],
        'double_congruent': con['double_congruent'],
        'spatial_congruent': con['spatial_congruent'],
        'double_incongruent': con['double_incongruent']
    }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def selective_stop_signal(design_matrix_columns):
    """ Contrasts for Stanford's selective_stop_signal protocol"""
    contrast_names = ['go_critical', 'go_noncritical', 'stop', 'ignore',
                      'go_critical-stop', 'go_noncritical-ignore',
                      'stop-ignore', 'ignore-stop']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'go_critical': con['go_critical'],
        'go_noncritical': con['go_noncritical'],
        'stop': con['stop'],
        'ignore': con['ignore'],
        'go_critical-stop': con['go_critical'] - con['stop'],
        'go_noncritical-ignore': con['go_noncritical'] - con['ignore'],
        'ignore-stop': con['ignore'] - con['stop'],
        'stop-ignore': con['stop'] - con['ignore']
    }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def stop_signal(design_matrix_columns):
    """Contrasts for the Stanford stop signal protocol"""
    contrast_names = ['go', 'stop', 'stop-go']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'go': con['go'],
        'stop': con['stop'],
        'stop-go': con['stop'] - con['go'],
    }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def stroop(design_matrix_columns):
    """Contrasts for the stanford stroop protocol"""
    contrast_names = ['congruent', 'incongruent', 'incongruent-congruent']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'congruent': con['congruent'],
        'incongruent': con['incongruent'],
        'incongruent-congruent': con['incongruent'] - con['congruent'],
    }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def lyon_lec2(design_matrix_columns):
    """Contrasts for the lyon lec2 protocol"""
    contrast_names = ['attend', 'unattend', 'attend-unattend']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'attend': con['attend'],
        'unattend': con['unattend'],
        'attend-unattend': con['attend'] - con['unattend'],
    }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def lyon_audi(design_matrix_columns):
    """Contrasts for the lyon audi protocol"""
    contrast_names = ['tear', 'suomi', 'yawn', 'human', 'music',
                      'reverse', 'speech', 'alphabet', 'cough', 'environment',
                      'laugh', 'animals',  'silence', 'tear-silence',
                      'suomi-silence',
                      'yawn-silence', 'human-silence', 'music-silence',
                      'reverse-silence', 'speech-silence', 'alphabet-silence',
                      'cough-silence', 'environment-silence',
                      'laugh-silence', 'animals-silence']

    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(name, con[name]) for name in contrast_names[:13]])
    for name in contrast_names[:12]:
        contrasts[name + '-silence'] = con[name] - con['silence']
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def lyon_visu(design_matrix_columns):
    """Contrasts for the lyon visu protocol"""
    contrast_names = ['scrambled', 'scene', 'tool', 'face', 'target_fruit',
                      'house', 'animal', 'characters', 'pseudoword',
                      'scene-scrambled', 'tool-scrambled',
                      'face-scrambled', 'house-scrambled', 'animal-scrambled',
                      'characters-scrambled', 'pseudoword-scrambled', ]
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    canonical_contrasts = ['scrambled', 'scene', 'tool', 'face',
                           'house', 'animal', 'characters', 'pseudoword']
    contrast = dict([(name, con[name]) for name in canonical_contrasts])
    # average = np.array([x for x in contrast.values()]).sum(0) * 1. / 8
    contrast['target_fruit'] = con['target_fruit']
    contrast['scene-scrambled'] = contrast['scene'] - contrast['scrambled']
    contrast['tool-scrambled'] = contrast['tool'] - contrast['scrambled']
    contrast['face-scrambled'] = contrast['face'] - contrast['scrambled']
    contrast['house-scrambled'] = contrast['house'] - contrast['scrambled']
    contrast['animal-scrambled'] = contrast['animal'] - contrast['scrambled']
    contrast['characters-scrambled'] =\
        contrast['characters'] - contrast['scrambled']
    contrast['pseudoword-scrambled'] =\
        contrast['pseudoword'] - contrast['scrambled']
    assert((sorted(contrast.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrast)
    _append_effects_interest_contrast(design_matrix_columns, contrast)
    return contrast


def lyon_lec1(design_matrix_columns):
    """Contrasts for the lec1 protocol"""
    contrast_names = ['pseudoword', 'word', 'random_string', 'word-pseudoword',
                      'word-random_string', 'pseudoword-random_string',
                      ]
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'pseudoword': con['pseudoword'],
        'word': con['word'],
        'random_string': con['random_string'],
        'word-pseudoword': con['word'] - con['pseudoword'],
        'word-random_string': con['word'] - con['random_string'],
        'pseudoword-random_string': con['pseudoword'] - con['random_string']
    }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def audio(design_matrix_columns):
    """Contrasts for the audio protocol"""
    contrast_names = [
        'animal', 'music', 'nature',
        'speech', 'tool', 'voice',
        'animal-others', 'music-others', 'nature-others',
        'speech-others', 'tool-others', 'voice-others',
        'mean-silence',
        'animal-silence', 'music-silence', 'nature-silence',
        'speech-silence', 'tool-silence', 'voice-silence',
        ]
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    others = (con['animal'] + con['music'] + con['nature'] +
              con['speech'] + con['tool'] + con['voice']) / 5
    contrasts = {
        'animal': con['animal'],
        'music': con['music'],
        'nature': con['nature'],
        'speech': con['speech'],
        'tool': con['tool'],
        'voice': con['voice'],
        'mean-silence': others - con['silence'],
        'animal-others': con['animal'] - others,
        'music-others': con['music'] - others,
        'nature-others': con['nature'] - others,
        'speech-others': con['speech'] - others,
        'tool-others': con['tool'] - others,
        'voice-others': con['voice'] - others,
        'animal-silence': con['animal'] - con['silence'],
        'music-silence': con['music'] - con['silence'],
        'nature-silence': con['nature'] - con['silence'],
        'speech-silence': con['speech'] - con['silence'],
        'tool-silence': con['tool'] - con['silence'],
        'voice-silence': con['voice'] - con['silence'],
        }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def lyon_mveb(design_matrix_columns):
    """ Contrasts for Lyon mveb localizer"""
    contrast_names = [
        'letter_occurrence_response', '2_letters_different', '2_letters_same',
        '4_letters_different', '4_letters_same',
        '6_letters_different', '6_letters_same',
        '2_letters_different-same',
        '4_letters_different-same', '6_letters_different-same',
        '6_letters_different-2_letters_different']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    #
    contrasts = dict([(key, con[key]) for key in contrast_names[1:7]])
    contrasts['letter_occurrence_response'] = con['response']
    contrasts['2_letters_different-same'] = con['2_letters_different'] -\
        con['2_letters_same']
    contrasts['4_letters_different-same'] = con['4_letters_different'] -\
        con['4_letters_same']
    contrasts['6_letters_different-same'] = con['6_letters_different'] -\
        con['6_letters_same']
    contrasts['6_letters_different-2_letters_different'] =\
        con['6_letters_different'] - con['2_letters_different']
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def lyon_mvis(design_matrix_columns):
    """ Contrasts for Lyon mvis localizer"""
    contrast_names = ['dot_displacement_response',
                      '2_dots-2_dots_control', '4_dots-4_dots_control',
                      '6_dots-6_dots_control', '6_dots-2_dots', 'dots-control']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    # contrasts = dict([(cname, con[cname]) for cname in contrast_names[:-4]])
    contrasts = {'dot_displacement_response': con['response']}
    contrasts['2_dots-2_dots_control'] = con['2_dots'] - con['2_dots_control']
    contrasts['4_dots-4_dots_control'] = con['4_dots'] - con['4_dots_control']
    contrasts['6_dots-6_dots_control'] = con['6_dots'] - con['6_dots_control']
    contrasts['6_dots-2_dots'] = con['6_dots'] - con['2_dots']
    contrasts['dots-control'] = con['6_dots'] + con['4_dots'] + con['2_dots']\
        - (con['2_dots_control'] + con['6_dots_control'] +
           con['4_dots_control'])
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def lyon_moto(design_matrix_columns):
    """ Contrasts for Lyon motor localizer"""
    contrast_names = [
        'instructions', 'finger_right-fixation', 'finger_left-fixation',
        'foot_left-fixation', 'foot_right-fixation', 'hand_left-fixation',
        'hand_right-fixation', 'saccade-fixation', 'tongue-fixation']
    elementary_contrasts = [
        'foot_left', 'foot_right', 'finger_right', 'finger_left',
        'saccade_left', 'saccade_right', 'hand_left', 'hand_right',
        'fixation_right', 'tongue_right', 'fixation_left',  'tongue_left']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    # avg = np.mean([con[cname] for cname in elementary_contrasts], 0)
    contrasts = {'instructions': con['instructions']}
    con['fixation'] = .5 * (con['fixation_left'] + con['fixation_right'])
    contrasts['finger_right-fixation'] = con['finger_right'] - con['fixation']
    contrasts['finger_left-fixation'] = con['finger_left'] - con['fixation']
    contrasts['foot_left-fixation'] = con['foot_left'] - con['fixation']
    contrasts['foot_right-fixation'] = con['foot_right'] - con['fixation']
    contrasts['hand_left-fixation'] = con['hand_left'] - con['fixation']
    contrasts['hand_right-fixation'] = con['hand_right'] - con['fixation']
    contrasts['saccade-fixation'] = con['saccade_left'] + con['saccade_right']\
        - 2 * con['fixation']
    contrasts['tongue-fixation'] = con['tongue_left'] + con['tongue_right']\
        - 2 * con['fixation']
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def lyon_mcse(design_matrix_columns):
    """ Contrasts for Lyon MCSE localizer"""
    contrast_names = [
        'high_salience_left', 'high_salience_right',
        'low_salience_left', 'low_salience_right',
        'high-low_salience', 'low-high_salience',
        'salience_left-right', 'salience_right-left',
        'low+high_salience']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'high_salience_left': con['hi_salience_left'],
        'high_salience_right': con['hi_salience_right'],
        'low_salience_left': con['low_salience_left'],
        'low_salience_right': con['low_salience_right'],
        'high-low_salience':
            con['hi_salience_left'] + con['hi_salience_right'] -
            con['low_salience_left'] - con['low_salience_right'],
        'low-high_salience':
            - con['hi_salience_left'] - con['hi_salience_right']
            + con['low_salience_left'] + con['low_salience_right'],
        'salience_left-right':
            con['hi_salience_left'] - con['hi_salience_right']
            + con['low_salience_left'] - con['low_salience_right'],
        'salience_right-left':
            - con['hi_salience_left'] + con['hi_salience_right']
            - con['low_salience_left'] + con['low_salience_right'],
        'low+high_salience':
            con['hi_salience_left'] + con['hi_salience_right']
            + con['low_salience_left'] + con['low_salience_right'],
    }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def bang(design_matrix_columns):
    """ Contrasts for bang experiment"""
    contrast_names = ['talk', 'no_talk', 'talk-no_talk']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {
        'talk': con['talk'],
        'no_talk': con['no_talk'],
        'talk-no_talk': con['talk'] - con['no_talk'],}
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def self_localizer(design_matrix_columns):
    """ Contrasts for self experiment"""
    contrast_names = [
        'encode_self-other', 'encode_other', 'encode_self',
        'instructions', 'false_alarm', 'correct_rejection',
        'recognition_hit', 'recognition_hit-correct_rejection',
        'recognition_self-other', 'recognition_self_hit',
        'recognition_other_hit'
    ]
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)

    try:
        recognition_hit = con['recognition_other_hit'] +\
            con['recognition_self_hit']
    except KeyError:
        if 'recognition_self_hit' in con.keys():
            recognition_hit = con['recognition_self_hit']
        elif 'recognition_other_hit' in con.keys():
            recognition_hit = con['recognition_other_hit']
        else:
            recognition_hit = con['recognition_other_no_response']
    try:
        correct_rejection = con['correct_rejection']
    except KeyError:
        correct_rejection = con['false_alarm']  #
    try:
        recognition_self_hit = con['recognition_self_hit']
    except KeyError:
        recognition_self_hit = con['recognition_self_miss']
    try:
        recognition_self = con['recognition_self_hit'] +\
            con['recognition_self_miss']
    except KeyError:
        if 'recognition_self_miss' in con.keys():
            recognition_self = con['recognition_self_miss']
        else:
            recognition_self = con['recognition_self_hit']
    try:
        recognition_other = con['recognition_other_hit'] +\
            con['recognition_other_miss']
    except KeyError:
        if 'recognition_other_hit' in con.keys():
            recognition_other = con['recognition_other_hit']
        else:
            recognition_other = con['recognition_other_miss']
    try:
        recognition_other_hit = con['recognition_other_hit']
    except KeyError:
        recognition_other_hit = con['recognition_other_miss']

    contrasts = {
        'encode_self-other': con['encode_self'] - con['encode_other'],
        'encode_other': con['encode_other'],
        'encode_self': con['encode_self'],
        'instructions': con['instructions'],
        'false_alarm': con['false_alarm'],
        'recognition_hit': recognition_hit,
        'recognition_self_hit': recognition_self_hit,
        'recognition_hit-correct_rejection':
            recognition_hit - correct_rejection,
        'correct_rejection': correct_rejection,
        'recognition_self-other': recognition_self - recognition_other,
        'recognition_other_hit': recognition_other_hit,
        }

    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def colour(design_matrix_columns):
    """ Contrasts for pain lcoalizer """
    if design_matrix_columns is None:
        return {'color': [], 'grey': [], 'color-grey': []}
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {'color': con['color'],
                 'grey': con['grey'],
                 'color-grey': con['color'] - con['grey'],
                 }
    return contrasts


def vstm(design_matrix_columns):
    """ contrasts for vstm task, Knops protocol"""
    contrast_names = [
       'vstm_linear',
       'vstm_constant',
       'vstm_quadratic']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    constant = np.ones(6)
    linear = np.linspace(-1, 1, 6)
    quadratic = linear ** 2 - (linear ** 2).mean()
    con = _elementary_contrasts(design_matrix_columns)
    response = np.array([con['response_num_%d' % i]
                        for i in range(1, 7)])
    contrasts = {
        'vstm_constant': np.dot(constant, response),
        'vstm_linear': np.dot(linear, response),
        'vstm_quadratic': np.dot(quadratic, response),
    }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def enumeration(design_matrix_columns):
    """ contrasts for vstm task, Knops protocol"""
    contrast_names = [
        'enumeration_linear',
        'enumeration_constant',
        'enumeration_quadratic']

    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    constant = np.ones(8)
    linear = np.linspace(-1, 1, 8)
    quadratic = linear ** 2 - (linear ** 2).mean()
    con = _elementary_contrasts(design_matrix_columns)
    response = np.array([con['response_num_%d' % i]
                         for i in range(1, 9)])
    contrasts = {
        'enumeration_constant': np.dot(constant, response),
        'enumeration_linear': np.dot(linear, response),
        'enumeration_quadratic': np.dot(quadratic, response),
    }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def pain_movie(design_matrix_columns):
    """ Contrast for pain task, TOM protocol"""
    contrast_names = ['movie_pain', 'movie_mental', 'movie_mental-pain',]
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {'movie_pain': con['pain'],
                 'movie_mental': con['mental'],
                 'movie_mental-pain': con['mental'] - con['pain'],
                 }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def emotional_pain(design_matrix_columns):
    """ Contrast for pain task, TOM protocol"""
    contrast_names = ['physical_pain', 'emotional_pain',
                      'emotional-physical_pain']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {'emotional_pain': con['emotional_pain'],
                 'physical_pain': con['physical_pain'],
                 'emotional-physical_pain':
                 con['emotional_pain'] - con['physical_pain'],
                 }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def theory_of_mind(design_matrix_columns):
    """ Contrast for tom task, TOM protocol"""
    contrast_names = ['belief', 'photo', 'belief-photo']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {'photo': con['photo'],
                 'belief': con['belief'],
                 'belief-photo': con['belief'] - con['photo'],
                 }
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def preferences(design_matrix_columns, domain):
    """Contrast for preference experiment"""
    if domain not in ['painting', 'house', 'face', 'food']:
        raise ValueError('Not a correct domain')
    contrast_names = ['%s_linear' % domain, '%s_constant' % domain,
                      '%s_quadratic' % domain]
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = dict([(key, con[key]) for key in contrast_names])
    assert((sorted(contrasts.keys()) == sorted(contrast_names)))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def _beta_contrasts(design_matrix_columns):
    """ Same as elementary contrasts, but retains only contrasts of interest"""
    con = _elementary_contrasts(design_matrix_columns)
    bad_names = tuple(['constant', 'rx', 'ry', 'rz', 'tx', 'ty', 'tz'] +
                      ['drift_%d' % d for d in range(20)] +
                      ['conf_%d' % d for d in range(20)])
    con_ = dict([(cname, cvalue) for (cname, cvalue) in con.items()
                if not cname.startswith(bad_names)])
    return con_


def mtt_we_relative(design_matrix_columns):
    """Contrast for MTT west-east task, relative setting"""
    contrast_list = [
        'we_average_reference',
        'we_all_space_cue',
        'we_all_time_cue',
        'we_westside_event',
        'we_eastside_event',
        'we_before_event',
        'we_after_event',
        'we_all_event_response',
        'we_all_space-time_cue',
        'we_all_time-space_cue',
        'we_average_event',
        'we_space_event',
        'we_time_event',
        'we_space-time_event',
        'we_time-space_event',
        'westside-eastside_event',
        'eastside-westside_event',
        'we_before-after_event',
        'we_after-before_event'
    ]
    if design_matrix_columns is None:
        return dict([(key, []) for key in contrast_list])

    con = _beta_contrasts(design_matrix_columns)
    contrasts = {
        'we_average_reference': con['we_all_reference'],
        'we_all_space_cue': con['we_all_space_cue'],
        'we_all_time_cue': con['we_all_time_cue'],
        'we_westside_event':
            con['we_westside_close_event']
            + con['we_westside_far_event'],
        'we_eastside_event':
            con['we_eastside_close_event']
            + con['we_eastside_far_event'],
        'we_before_event':
            con['we_before_close_event']
            + con['we_before_far_event'],
        'we_after_event':
            con['we_after_close_event']
            + con['we_after_far_event'],
        'we_all_event_response': con['we_all_event_response']}

    contrasts['we_all_space-time_cue'] =\
        contrasts['we_all_space_cue'] - contrasts['we_all_time_cue']
    contrasts['we_all_time-space_cue'] = - contrasts['we_all_space-time_cue']
    contrasts['we_space_event'] =\
        contrasts['we_westside_event'] + contrasts['we_eastside_event']
    contrasts['we_time_event'] =\
        contrasts['we_before_event'] + contrasts['we_after_event']
    contrasts['we_average_event'] =\
        contrasts['we_space_event'] + contrasts['we_time_event']
    contrasts['we_space-time_event'] =\
        contrasts['we_space_event'] - contrasts['we_time_event']
    contrasts['we_time-space_event'] = - contrasts['we_space-time_event']
    contrasts['westside-eastside_event'] =\
        contrasts['we_westside_event'] - contrasts['we_eastside_event']
    contrasts['eastside-westside_event'] =\
        - contrasts['westside-eastside_event']
    contrasts['we_before-after_event'] =\
        contrasts['we_before_event'] - contrasts['we_after_event']
    contrasts['we_after-before_event'] = - contrasts['we_before-after_event']
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts

def mtt_sn_relative(design_matrix_columns):
    """Contrast for MTT south-north task, relative setting"""
    contrast_list = [
        'sn_average_reference',
        'sn_all_space_cue',
        'sn_all_time_cue',
        'sn_southside_event',
        'sn_northside_event',
        'sn_before_event',
        'sn_after_event',
        'sn_all_event_response',
        'sn_all_space-time_cue',
        'sn_all_time-space_cue',
        'sn_average_event',
        'sn_space_event',
        'sn_time_event',
        'sn_space-time_event',
        'sn_time-space_event',
        'northside-southside_event',
        'southside-northside_event',
        'sn_before-after_event',
        'sn_after-before_event'
    ]
    if design_matrix_columns is None:
        return dict([(key, []) for key in contrast_list])

    con = _beta_contrasts(design_matrix_columns)
    contrasts = {
        'sn_average_reference': con['sn_all_reference'],
        'sn_all_space_cue': con['sn_all_space_cue'],
        'sn_all_time_cue': con['sn_all_time_cue'],
        'sn_southside_event':
            con['sn_southside_close_event']
            + con['sn_southside_far_event'],
        'sn_northside_event':
            con['sn_northside_close_event']
            + con['sn_northside_far_event'],
        'sn_before_event':
            con['sn_before_close_event']
            + con['sn_before_far_event'],
        'sn_after_event':
            con['sn_after_close_event']
            + con['sn_after_far_event'],
        'sn_all_event_response': con['sn_all_event_response']}

    contrasts['sn_all_space-time_cue'] =\
        contrasts['sn_all_space_cue'] - contrasts['sn_all_time_cue']
    contrasts['sn_all_time-space_cue'] = - contrasts['sn_all_space-time_cue']
    contrasts['sn_space_event'] =\
        contrasts['sn_southside_event'] + contrasts['sn_northside_event']
    contrasts['sn_time_event'] =\
        contrasts['sn_before_event'] + contrasts['sn_after_event']
    contrasts['sn_average_event'] =\
        contrasts['sn_space_event'] + contrasts['sn_time_event']
    contrasts['sn_space-time_event'] =\
        contrasts['sn_space_event'] - contrasts['sn_time_event']
    contrasts['sn_time-space_event'] = - contrasts['sn_space-time_event']
    contrasts['southside-northside_event'] =\
        contrasts['sn_southside_event'] - contrasts['sn_northside_event']
    contrasts['northside-southside_event'] =\
        - contrasts['southside-northside_event']
    contrasts['sn_before-after_event'] =\
        contrasts['sn_before_event'] - contrasts['sn_after_event']
    contrasts['sn_after-before_event'] = - contrasts['sn_before-after_event']
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def retino(design_matrix_columns):
    """ Contrast for retino experiment """
    if design_matrix_columns is None:
        return {'cos': [], 'sin': [], 'effects_interest': []}
    con = _elementary_contrasts(design_matrix_columns)
    contrasts = {'cos': con['cos'],
                 'sin': con['sin'],
                 'effects_interest': np.vstack((con['cos'], con['sin'])),
                 }
    return contrasts


def rsvp_language(design_matrix_columns):
    """ Contrasts for RSVP language localizer"""
    contrast_names = [
        'complex', 'simple', 'jabberwocky', 'word_list',
        'pseudoword_list', 'consonant_string', 'complex-simple',
        'sentence-jabberwocky', 'sentence-word',
        'word-consonant_string', 'jabberwocky-pseudo',
        'word-pseudo', 'pseudo-consonant_string',
        'sentence-consonant_string', 'simple-consonant_string',
        'complex-consonant_string', 'sentence-pseudo', 'probe',
        'jabberwocky-consonant_string']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])

    con = _elementary_contrasts(design_matrix_columns)
    con['complex'] = con['complex_sentence']
    con['simple'] = con['simple_sentence']
    contrasts = {
        'complex': con['complex'],
        'simple': con['simple'],
        'probe': con['probe'],
        'jabberwocky': con['jabberwocky'],
        'word_list': con['word_list'],
        'pseudoword_list': con['pseudoword_list'],
        'consonant_string': con['consonant_strings'],
        'complex-simple': con['complex'] - con['simple'],
        'sentence-jabberwocky': (con['complex'] + con['simple']
                                 - 2 * con['jabberwocky']),
        'sentence-word': (con['complex'] + con['simple'] -
                          2 * con['word_list']),
        'word-consonant_string': con['word_list'] - con['consonant_strings'],
        'jabberwocky-pseudo': con['jabberwocky'] - con['pseudoword_list'],
        'jabberwocky-consonant_string':
            con['jabberwocky'] - con['consonant_strings'],
        'word-pseudo': con['word_list'] - con['pseudoword_list'],
        'pseudo-consonant_string':
            con['pseudoword_list'] - con['consonant_strings'],
        'sentence-consonant_string': (con['complex'] + con['simple']
                                      - 2 * con['consonant_strings']),
        'simple-consonant_string': con['simple'] - con['consonant_strings'],
        'complex-consonant_string': con['complex'] - con['consonant_strings'],
        'sentence-pseudo':
            con['complex'] + con['simple'] - 2 * con['pseudoword_list']
    }
    assert(sorted(contrasts.keys()) == sorted(contrast_names))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def archi_social(design_matrix_columns):
    contrast_names = [
        'triangle_mental-random', 'false_belief-mechanistic_audio',
        'mechanistic_audio', 'false_belief-mechanistic_video',
        'mechanistic_video', 'false_belief-mechanistic',
        'speech-non_speech', 'triangle_mental', 'triangle_random',
        'false_belief_audio', 'false_belief_video',
        'speech_sound', 'non_speech_sound']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])

    con = _elementary_contrasts(design_matrix_columns)

    # and more complex / interesting ones
    contrasts = {
        'triangle_mental': con['triangle_intention'],
        'triangle_random': con['triangle_random'],
        'false_belief_audio': con['false_belief_audio'],
        'mechanistic_audio': con['mechanistic_audio'],
        'false_belief_video': con['false_belief_video'],
        'mechanistic_video': con['mechanistic_video'],
        'speech_sound': con['speech'],
        'non_speech_sound': con['non_speech'],
        'triangle_mental-random':
            con['triangle_intention'] - con['triangle_random'],
        'false_belief-mechanistic_audio':
            con['false_belief_audio'] - con['mechanistic_audio'],
        'false_belief-mechanistic_video':
            con['false_belief_video'] - con['mechanistic_video'],
        'speech-non_speech': con['speech'] - con['non_speech'],
        'mechanistic_video': con['mechanistic_video'],
        'mechanistic_audio': con['mechanistic_audio'], }
    contrasts['false_belief-mechanistic'] =\
        contrasts['false_belief-mechanistic_audio'] +\
        contrasts['false_belief-mechanistic_video']

    assert(sorted(contrasts.keys()) == sorted(contrast_names))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def archi_spatial(design_matrix_columns):
    contrast_names = [
        'saccades', 'rotation_hand', 'rotation_side', 'object_grasp',
        'object_orientation', 'hand-side', 'grasp-orientation']
    if design_matrix_columns is None:
        return dict([(name, []) for name in contrast_names])

    contrasts = _elementary_contrasts(design_matrix_columns)

    # more interesting contrasts
    contrasts = {
        'saccades': contrasts['saccade'],
        'rotation_hand': contrasts['rotation_hand'],
        'rotation_side': contrasts['rotation_side'],
        'object_grasp': contrasts['object_grasp'],
        'object_orientation': contrasts['object_orientation'],
        'hand-side': contrasts['rotation_hand'] - contrasts['rotation_side'],
        'grasp-orientation': (contrasts['object_grasp'] -
                              contrasts['object_orientation'])}
    assert(sorted(contrasts.keys()) == sorted(contrast_names))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def archi_standard(design_matrix_columns, new=True):
    contrast_names = [
        'audio_left_button_press', 'audio_right_button_press',
        'video_left_button_press', 'video_right_button_press',
        'left-right_button_press', 'right-left_button_press',
        'listening-reading', 'reading-listening',
        'motor-cognitive', 'cognitive-motor', 'reading-checkerboard',
        'horizontal-vertical', 'vertical-horizontal',
        'horizontal_checkerboard', 'vertical_checkerboard',
        'audio_sentence', 'video_sentence',
        'audio_computation', 'video_computation',
        'sentences', 'computation',
        'computation-sentences', 'sentences-computation',
    ]
    if design_matrix_columns is None:
        return dict([(x, []) for x in contrast_names])

    contrasts = _elementary_contrasts(design_matrix_columns)

    # and more complex/ interesting ones
    contrasts['audio_left_button_press'] = contrasts['audio_left_hand']
    contrasts['audio_right_button_press'] = contrasts['audio_right_hand']
    contrasts['video_left_button_press'] = contrasts['video_left_hand']
    contrasts['video_right_button_press'] = contrasts['video_right_hand']
    contrasts['audio'] = (contrasts['audio_left_hand'] +
                          contrasts['audio_right_hand'] +
                          contrasts['audio_computation'] +
                          contrasts['audio_sentence'])
    contrasts['audio_sentence'] = contrasts['audio_sentence']
    contrasts['video_sentence'] = contrasts['video_sentence']
    contrasts['audio_computation'] = contrasts['audio_computation']
    contrasts['video_computation'] = contrasts['video_computation']
    contrasts['video'] =\
        contrasts['video_left_hand'] + contrasts['video_right_hand'] + \
        contrasts['video_computation'] + contrasts['video_sentence']
    contrasts['left_button_press'] = (
        contrasts['audio_left_hand'] + contrasts['video_left_hand'])
    contrasts['right_button_press'] = (
        contrasts['audio_right_hand'] + contrasts['video_right_hand'])
    contrasts['computation'] =\
        contrasts['audio_computation'] + contrasts['video_computation']
    contrasts['sentences'] =\
        contrasts['audio_sentence'] + contrasts['video_sentence']
    contrasts['horizontal-vertical'] =\
        contrasts['horizontal_checkerboard']\
        - contrasts['vertical_checkerboard']
    contrasts['vertical-horizontal'] =\
        contrasts['vertical_checkerboard']\
        - contrasts['horizontal_checkerboard']
    contrasts['left-right_button_press'] = (
        contrasts['left_button_press'] - contrasts['right_button_press'])
    contrasts['right-left_button_press'] = (
        contrasts['right_button_press'] - contrasts['left_button_press'])
    contrasts['motor-cognitive'] = (
        contrasts['left_button_press'] + contrasts['right_button_press'] -
        contrasts['computation'] - contrasts['sentences'])
    contrasts['cognitive-motor'] = -(
        contrasts['left_button_press'] + contrasts['right_button_press'] -
        contrasts['computation'] - contrasts['sentences'])
    contrasts['listening-reading'] =\
        contrasts['audio'] - contrasts['video']
    contrasts['reading-listening'] =\
        contrasts['video'] - contrasts['audio']
    contrasts['computation-sentences'] = contrasts['computation'] -  \
        contrasts['sentences']
    contrasts['sentences-computation'] = contrasts['sentences'] -\
        contrasts['computation']
    contrasts['reading-checkerboard'] = contrasts['video_sentence'] - \
        contrasts['horizontal_checkerboard']

    contrasts = dict([(x, contrasts[x]) for x in contrast_names])
    assert(sorted(contrasts.keys()) == sorted(contrast_names))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def archi_emotional(design_matrix_columns):
    contrast_names = [
        'face_gender', 'face_control', 'face_trusty',
        'expression_intention', 'expression_gender', 'expression_control',
        'trusty_and_intention-control', 'trusty_and_intention-gender',
        'expression_gender-control', 'expression_intention-control',
        'expression_intention-gender', 'face_trusty-control',
        'face_gender-control', 'face_trusty-gender']
    if design_matrix_columns is None:
        return dict([(x, []) for x in contrast_names])

    contrasts = _elementary_contrasts(design_matrix_columns)

    # and more complex/ interesting ones
    contrasts = {
        'face_gender': contrasts['face_gender'],
        'face_control': contrasts['face_control'],
        'face_trusty': contrasts['face_trusty'],
        'expression_intention': contrasts['expression_intention'],
        'expression_gender': contrasts['expression_gender'],
        'expression_control': contrasts['expression_control'],
        'face_trusty-gender': (
            contrasts['face_trusty'] - contrasts['face_gender']),
        'face_gender-control': (
            contrasts['face_gender'] - contrasts['face_control']),
        'face_trusty-control': (
            contrasts['face_trusty'] - contrasts['face_control']),
        'expression_intention-gender': (
            contrasts['expression_intention'] -
            contrasts['expression_gender']),
        'expression_intention-control': (
            contrasts['expression_intention'] -
            contrasts['expression_control']),
        'expression_gender-control': (
            contrasts['expression_gender'] - contrasts['expression_control'])}
    contrasts['trusty_and_intention-gender'] = (
        contrasts['face_trusty-gender'] +
        contrasts['expression_intention-gender'])
    contrasts['trusty_and_intention-control'] = (
        contrasts['face_trusty-control'] +
        contrasts['expression_intention-control'])
    assert(sorted(contrasts.keys()) == sorted(contrast_names))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def hcp_emotion(design_matrix_columns=None):
    contrast_names = ['face', 'shape', 'face-shape', 'shape-face']
    if design_matrix_columns is None:
        return dict([(x, []) for x in contrast_names])
    n_columns = len(design_matrix_columns)
    contrasts = {}
    for i in range(n_columns):
        contrasts['%s' % design_matrix_columns[i].lower()] =\
            np.eye(n_columns)[i]
    contrasts = dict([(key, contrasts[key.lower()])
                     for key in ['face', 'shape']])
    contrasts = {'face-shape': contrasts['face'] - contrasts['shape'],
                 'shape-face': contrasts['shape'] - contrasts['face'],
                 'face': contrasts['face'],
                 'shape': contrasts['shape'], }
    assert(sorted(contrasts.keys()) == sorted(contrast_names))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def hcp_gambling(design_matrix_columns):
    contrast_names = [
        'punishment-reward', 'reward-punishment', 'punishment', 'reward']
    if design_matrix_columns is None:
        return dict([(x, []) for x in contrast_names])
    n_columns = len(design_matrix_columns)
    contrasts = {}
    for i in range(n_columns):
        contrasts['%s' % design_matrix_columns[i].lower()] =\
            np.eye(n_columns)[i]
    contrasts = dict([(key, contrasts[key])
                     for key in ['punishment', 'reward']])
    contrasts = {
        'punishment-reward': contrasts['punishment'] - contrasts['reward'],
        'reward-punishment': contrasts['reward'] - contrasts['punishment'],
        'punishment': contrasts['punishment'],
        'reward': contrasts['reward']}
    assert(sorted(contrasts.keys()) == sorted(contrast_names))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def hcp_language(design_matrix_columns):
    contrast_names = ['math-story', 'story-math', 'math', 'story']
    if design_matrix_columns is None:
        return dict([(x, []) for x in contrast_names])
    n_columns = len(design_matrix_columns)
    contrasts = {}
    for i in range(n_columns):
        contrasts['%s' % design_matrix_columns[i].lower()] =\
            np.eye(n_columns)[i]
    contrasts = dict([(key, contrasts[key]) for key in ['math', 'story']])
    contrasts = {
        'math-story': contrasts['math'] - contrasts['story'],
        'story-math': contrasts['story'] - contrasts['math'],
        'math': contrasts['math'],
        'story': contrasts['story']}
    assert(sorted(contrasts.keys()) == sorted(contrast_names))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def hcp_motor(design_matrix_columns):
    contrast_names = [
        'left_hand', 'right_hand', 'left_foot', 'right_foot',
        'tongue', 'tongue-avg', 'left_hand-avg', 'right_hand-avg',
        'left_foot-avg', 'right_foot-avg', 'cue']
    if design_matrix_columns is None:
        return dict([(x, []) for x in contrast_names])
    n_columns = len(design_matrix_columns)
    contrasts = {}
    for i in range(n_columns):
        contrasts['%s' % design_matrix_columns[i].lower()] =\
            np.eye(n_columns)[i]
    contrasts['Average'] = (
        contrasts['left_hand'] + contrasts['right_hand'] +
        contrasts['left_foot'] +
        contrasts['right_foot'] + contrasts['tongue']) / 5
    contrasts = {
        'cue': contrasts['cue'],
        'left_hand': contrasts['left_hand'],
        'right_hand': contrasts['right_hand'],
        'left_foot': contrasts['left_foot'],
        'right_foot': contrasts['right_foot'],
        'tongue': contrasts['tongue'],
        'left_hand-avg': contrasts['left_hand'] - contrasts['Average'],
        'right_hand-avg': contrasts['right_hand'] - contrasts['Average'],
        'left_foot-avg': contrasts['left_foot'] - contrasts['Average'],
        'right_foot-avg': contrasts['right_foot'] - contrasts['Average'],
        'tongue-avg': contrasts['tongue'] - contrasts['Average']
    }
    assert(sorted(contrasts.keys()) == sorted(contrast_names))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def hcp_relational(design_matrix_columns):
    contrast_names = ['relational', 'relational-match', 'match']
    if design_matrix_columns is None:
        return dict([(x, []) for x in contrast_names])
    n_columns = len(design_matrix_columns)
    contrasts = {}
    for i in range(n_columns):
        contrasts['%s' % design_matrix_columns[i].lower()] =\
            np.eye(n_columns)[i]
    contrasts = dict([(key, contrasts[key]) for key in
                      ['relational', 'control']])
    contrasts = {
        'match': contrasts['control'],
        'relational': contrasts['relational'],
        'relational-match': contrasts['relational'] - contrasts['control']}
    assert(sorted(contrasts.keys()) == sorted(contrast_names))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def hcp_social(design_matrix_columns):
    contrast_names = ['mental-random', 'mental', 'random']
    if design_matrix_columns is None:
        return dict([(x, []) for x in contrast_names])
    n_columns = len(design_matrix_columns)
    contrasts = {}
    for i in range(n_columns):
        contrasts['%s' % design_matrix_columns[i].lower()] =\
            np.eye(n_columns)[i]
    contrasts = dict([(key, contrasts[key]) for key in ['mental', 'random']])
    contrasts = {
        'mental-random': contrasts['mental'] - contrasts['random'],
        'random': contrasts['random'],
        'mental': contrasts['mental'], }
    assert(sorted(contrasts.keys()) == sorted(contrast_names))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts


def hcp_wm(design_matrix_columns):
    contrast_names = ['2back-0back', '0back-2back', 'body-avg',
                      'face-avg', 'place-avg', 'tools-avg',
                      '0back_body', '2back_body', '0back_face', '2back_face',
                      '0back_tools', '2back_tools', '0back_place',
                      '2back_place']
    if design_matrix_columns is None:
        return dict([(x, []) for x in contrast_names])
    n_columns = len(design_matrix_columns)
    contrasts = {}
    for i in range(n_columns):
        contrasts['%s' % design_matrix_columns[i].lower()] =\
            np.eye(n_columns)[i]
    contrasts = dict([(key, contrasts[key]) for key in [
        '2back_body', '0back_body', '2back_face', '0back_face', '2back_tools',
        '0back_tools', '0back_place', '2back_place']])
    contrasts['2back'] = (contrasts['2back_body'] + contrasts['2back_face'] +
                          contrasts['2back_tools'] + contrasts['2back_place'])
    contrasts['0back'] = (contrasts['0back_body'] + contrasts['0back_face'] +
                          contrasts['0back_tools'] + contrasts['0back_place'])
    contrasts['body'] = (contrasts['2back_body'] + contrasts['0back_body']) / 2
    contrasts['face'] = (contrasts['2back_face'] + contrasts['0back_face']) / 2
    contrasts['place'] = (
        contrasts['2back_place'] + contrasts['0back_place']) / 2
    contrasts['tools'] = (
        contrasts['2back_tools'] + contrasts['0back_tools']) / 2
    contrasts['average'] = (contrasts['2back'] + contrasts['0back']) / 8
    contrasts = {
        '0back_body': contrasts['0back_body'],
        '2back_body': contrasts['2back_body'],
        '0back_face': contrasts['0back_face'],
        '2back_face': contrasts['2back_face'],
        '0back_tools': contrasts['0back_tools'],
        '2back_tools': contrasts['2back_tools'],
        '0back_place': contrasts['0back_place'],
        '2back_place': contrasts['2back_place'],
        '2back-0back': contrasts['2back'] - contrasts['0back'],
        '0back-2back': contrasts['0back'] - contrasts['2back'],
        'body-avg': contrasts['body'] - contrasts['average'],
        'face-avg': contrasts['face'] - contrasts['average'],
        'place-avg': contrasts['place'] - contrasts['average'],
        'tools-avg': contrasts['tools'] - contrasts['average']}
    assert(sorted(contrasts.keys()) == sorted(contrast_names))
    _append_derivative_contrast(design_matrix_columns, contrasts)
    _append_effects_interest_contrast(design_matrix_columns, contrasts)
    return contrasts
