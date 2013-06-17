# coding=iso-8859-1

# PyCryptsy Example
#
# Copyright © 2013 Scott Alfter
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from PyCryptsy import PyCryptsy

api=PyCryptsy('public_key_goes_here', 'private_key_goes_here')

# currencies to trade

src="YAC"
dest="BTC"

# trade multiplier (set to 1 to trade at lowest buy price)

multiplier=1.01

# get market ID

result = api.Query("getmarkets", {});
for i, market in enumerate(result["return"]):
  if market["primary_currency_code"]==src and market["secondary_currency_code"]==dest:
    mkt_id=market["marketid"]

# get target 

result = api.Query("marketorders", {"marketid": mkt_id})
target=float(result["return"]["buyorders"][0]["buyprice"])*multiplier

# get available balance

result = api.Query("getinfo", {});
avail=float(result["return"]["balances_available"][src])

# trade 10% of available balance

result=api_query("createorder", {"marketid": mkt_id, "ordertype": "Sell", "quantity": avail/10, "price": target})
print result
