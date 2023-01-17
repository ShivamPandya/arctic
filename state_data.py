VALID_STATES = {"undersized", "idling", "optimized", "under_pressure", "waiting_for_data"}

def generate_ros_data(state="random", cpu_score=None, io_score=None, memory_score=None):
    """Generate ros_data based on state"""
    new_text = ""
    metrics_json = {}
    if state not in VALID_STATES:
        raise ValueError(
            "Correct values are: random, optimized, Idling, Under pressure, "
            "Undersized, Waiting for data"
        )

    state = state.lower()

    if state == "optimized":
        metrics_json["kernel.all.cpu.idle"] = "0.997"
        metrics_json['kernel.all.pressure.cpu.some.avg["1 minute"]'] = "0.060"
        metrics_json['kernel.all.pressure.io.full.avg ["1 minute"]'] = "0.000"
        metrics_json['kernel.all.pressure.io.some.avg ["1 minute"]'] = "0.000"
        metrics_json['kernel.all.pressure.memory.full.avg ["1 minute"]'] = "0.000"
        metrics_json['kernel.all.pressure.memory.some.avg ["1 minute"]'] = "0.000"
        metrics_json["mem.util.available"] = "525040.000"

    elif state == "idling":
        metrics_json["kernel.all.cpu.idle"] = "1.997"
        metrics_json['kernel.all.pressure.cpu.some.avg["1 minute"]'] = "0.060"
        metrics_json['kernel.all.pressure.io.full.avg ["1 minute"]'] = "0.000"
        metrics_json['kernel.all.pressure.io.some.avg ["1 minute"]'] = "0.000"
        metrics_json['kernel.all.pressure.memory.full.avg ["1 minute"]'] = "0.000"
        metrics_json['kernel.all.pressure.memory.some.avg ["1 minute"]'] = "0.000"
        metrics_json["mem.util.available"] = "825040.000"

    elif state == "under_pressure":
        metrics_json["kernel.all.cpu.idle"] = "1.797"
        metrics_json['kernel.all.pressure.cpu.some.avg["1 minute"]'] = "21.060"
        metrics_json['kernel.all.pressure.io.full.avg ["1 minute"]'] = "21.000"
        metrics_json['kernel.all.pressure.io.some.avg ["1 minute"]'] = "210.000"
        metrics_json['kernel.all.pressure.memory.full.avg ["1 minute"]'] = "21.000"
        metrics_json['kernel.all.pressure.memory.some.avg ["1 minute"]'] = "21.000"
        metrics_json["mem.util.available"] = "725040.000"

    elif state == "undersized":
        metrics_json["kernel.all.cpu.idle"] = "0.197"
        metrics_json['kernel.all.pressure.cpu.some.avg["1 minute"]'] = "21.060"
        metrics_json['kernel.all.pressure.io.full.avg ["1 minute"]'] = "21.000"
        metrics_json['kernel.all.pressure.io.some.avg ["1 minute"]'] = "210.000"
        metrics_json['kernel.all.pressure.memory.full.avg ["1 minute"]'] = "21.000"
        metrics_json['kernel.all.pressure.memory.some.avg ["1 minute"]'] = "21.000"
        metrics_json["mem.util.available"] = "25040.000"

    elif state == "Waiting_for_data":
        return new_text

    suffix = {
        "mem.util.available": "Kbyte",
        "mem.physmem": "Kbyte",
        "disk.dev.total": "count / sec",
    }

    metrics_json["hinv.ncpu"] = "2.000"
    metrics_json["disk.dev.total"] = '["xvda"] 0.314'
    metrics_json["mem.physmem"] = "825740.000"

    for key, val in metrics_json.items():
        if key in suffix:
            new_text += f"{key} {val} {suffix[key]}\n"
        else:
            new_text += f"{key} {val} none\n"

    return new_text
