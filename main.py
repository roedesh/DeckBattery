import re
import subprocess


def get_value(report, field):
    regex_result = re.search(f'{field}:[^a-zA-Z0-9]+([a-zA-Z0-9.% ]+)', str(report))
    if regex_result:
        return regex_result.groups()[0]
    return "N/A"

class Plugin:
    async def get_battery_report(self, *args):
        report = subprocess.check_output(["upower", "-i", "/org/freedesktop/UPower/devices/battery_BAT1"])
        
        return {
            "model": get_value(report, "model"),
            "percentage": get_value(report, "percentage"),
            "capacity": get_value(report, "capacity"),
            "warningLevel": get_value(report, "warning-level").capitalize(),
            "state": get_value(report, "state").capitalize(),
            "energy": get_value(report, "energy"),
            "energyEmpty": get_value(report, "energy-empty"),
            "energyFull": get_value(report, "energy-full"),
            "energyFullDesign": get_value(report, "energy-full-design"),
            "energyRate": get_value(report, "energy-rate"),
            "timeToEmpty": get_value(report, "time to empty"),
            "timeToFull": get_value(report, "time to full"),
            "voltage": get_value(report, "voltage"),
        }