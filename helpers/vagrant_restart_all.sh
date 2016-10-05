#!/bin/bash
ssh 10.0.0.1 'cd ~/broeval; vagrant halt /bro1[1-4]/; vagrant up /bro1[1-4]/'
ssh 10.0.0.2 'cd ~/broeval; vagrant halt /bro2[1-4]/; vagrant up /bro2[1-4]/'
ssh 10.0.0.3 'cd ~/broeval; vagrant halt /bro3[1-4]/; vagrant up /bro3[1-4]/'
