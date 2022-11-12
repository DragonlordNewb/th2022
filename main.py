# Copyright 2022 Lux Bodell and Samuel "Reyna" Daniels.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Tonka Hacks 2022 Project - Sustainability

# First, import all of the packages we're gonna need to assemble the app. These
# were created by copying the package directory from site-packages to the
# /packages/ module in this app's directory, then importing the __init__ file
# therein, as well as some other modules used by the application.

import intelligence # for natural language processing and data analysis
import settings     # for data about the application appearance, etc.
import os           # for file and directory handling
import gui          # for UI control

def initialize():
    gui.setupUI()
    gui.startUI()

if __name__ == "__main__":
    initialize()
