import random

def _checksum(railcar_number):
    """
    Calculate checksum for a railcar number
    @param {number} railcar_number
    @return {number} checksum
    """
    railcar_number = str( int( railcar_number) );
    digit = 0
    total = 0

    for i in range(0, len(railcar_number), 1):
        digit = int(railcar_number[i]) << (i & 1);
        total += digit - (digit > 9) * 9;
    
    #zero should be returned if the sum % 10 === 0
    return 10 - (total % 10 or 10);  

def create_railcar_number(railcar_number=random.randint(10000, 999999)):
    """
    Function createRailCarNumber create a valid railcar number.
    @param {number} railcarnumber, default value randomly generated integer 10000 to 999999
    @return {string} railcar number with a checksum suffix
    """
    check_suffix = _checksum(railcar_number)
    return "%s-%s" % (railcar_number, check_suffix)

def validate_railcar_number(railcar):
    """
    Validate railcar number
    @param {string} railcar number with a checksum suffix
    @return {boolean} True if railcar number is valid, False is not
    """    
    railcar_number, check_suffix =  railcar.split('-')    
    return str(_checksum(railcar_number)) == check_suffix

def humanize_bytes(nbytes):
    """
    Humanize bytes to human readable format
    humansize(2**20) -> '1 MB'
    @param {int} nbytes
    @return {string} return human readable format 
    """
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

    if nbytes == 0: return '0 B'
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
      nbytes /= 1024.
      i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])