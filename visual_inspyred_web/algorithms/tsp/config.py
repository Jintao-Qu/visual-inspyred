def _init():
    global _config_dict
    _config_dict = {}
    _config_dict["self-adaption"] = True
    _config_dict["tao_rate"] = 3/90

    _config_dict["filename"] = "data/carcount.txt"#insect15,insect_b,dowjones, eog, carcount, LSF5_10
    _config_dict["pop_size"] = 4
    _config_dict["max_evaluations"] = 400
    _config_dict["wmin"] = 30
    _config_dict["wmax"] = 30
    _config_dict["gbest"] = 0x3f3f3f3f


    _config_dict["bounder"] = "attach"#attach, MOD, CRAZY
    _config_dict["CRAZY"] = 0.09
    _config_dict["IF_Elite"] = False
    _config_dict["Elite_list"] = []

    _config_dict["CRAZY_PSO"] = 0.0

    _config_dict["t_lastupdate"] = 0
    _config_dict["t_updated"] = 0
    _config_dict["TCONV"] = 0x3f3f3f3f

    _config_dict["FORCE_NOT_OVERLAP"] = True
    _config_dict["DTW_ALGO"] = "CUSTOM_DTW"# CUSTOM_DTW, Pierre_DTW

    _config_dict["SHOW_CONVERGENCE_RATE"] = False
    _config_dict["CONVERGENCE_RATE_LIST"] = []

    _config_dict["SHOW_MOTIF"] = True
    _config_dict["SHOW_SWARM_DISTRIBUTION"] = False
    _config_dict["SHOW_INIT_SWARM"] = False
    _config_dict["SHOW_SWARM_CYCLE"] = 0x3f3f3f3f
    _config_dict["Xi"] = []
    _config_dict["Xj"] = []
    _config_dict["Wi"] = []
    _config_dict["Wj"] = []

    _config_dict["CHAOS_ALGO"] = "None" #logistic, cube, None
    _config_dict["CHAOS_SEED"] = [0.3, 0.45, 0.35, 0.2]

def set_value(name, value):
    _config_dict[name] = value

def get_value(name):
    return _config_dict[name]