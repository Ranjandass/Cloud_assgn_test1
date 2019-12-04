# Copyright Google Inc. 2017
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging
import concurrent
import time
from bokeh.plotting import figure
from bokeh.io import show

# Hide some noisy warnings
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

modules = [modules.air.Module(), modules.temperature.Module(), modules.population.Module(), modules.precipitation.Module()]


#start


x=[1,2,3,4,5]
y=[3,4,5,6,7]

fig=figure(plot_height=500,plot_width=1000)
fig.line(x=x,y=y)
show(fig)
#end
