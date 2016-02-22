import os
from fabric.api import run, env, cd, roles, lcd, local, sudo

def gp():
	lcd("/home/neyron/Projects/Kairos/")
	local("sudo git add .")
	local("sudo git commit")
	local("sudo git push Kairos master")