string = re.sub('<D0_1e28 value="(\d.*\.\d.*?)" />',
         '<D0_1e28 value="' + str(D0) + '" />', string)
string = re.sub('<Delta value="(\d.*\.\d.*?)" />',
         '<Delta value="' + str(delta) + '" />', string)