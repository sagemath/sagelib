"""
Root system data for type I
"""
#*****************************************************************************
#       Copyright (C) 2008-2009 Nicolas M. Thiery <nthiery at users.sf.net>, 
#
#  Distributed under the terms of the GNU General Public License (GPL)
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from cartan_type import CartanType_standard_finite, CartanType_simple
class CartanType(CartanType_standard_finite, CartanType_simple):
    def __init__(self, n):
        """
        EXAMPLES::
        
            sage: ct = CartanType(['I',5])
            sage: ct
            ['I', 5]
            sage: ct._repr_(compact = True)
            'I5'
            sage: ct.rank()
            2
            sage: ct.index_set()
            [1, 2]

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            True
            sage: ct.is_affine()
            False
            sage: ct.is_crystalographic()
            False
            sage: ct.is_simply_laced()
            False

        TESTS::

            sage: ct == loads(dumps(ct))
            True
        """
        assert n >= 1
        CartanType_standard_finite.__init__(self, "I", n)

    def rank(self):
        """
        Type `I_p` is of rank 2

        EXAMPLES::
            sage: CartanType(['I', 5]).rank()
            2
        """
        return 2

    def index_set(self):
        """
        Type `I_p` is of rank 2

        EXAMPLES::
            sage: CartanType(['I', 5]).index_set()
            [1, 2]
        """
        return [1, 2]
