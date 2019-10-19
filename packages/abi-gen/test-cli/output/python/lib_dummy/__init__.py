"""Generated wrapper for LibDummy Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

from eth_utils import to_checksum_address
from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider

from zero_ex.contract_wrappers.bases import ContractMethod, Validator
from zero_ex.contract_wrappers.tx_params import TxParams


# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for LibDummy below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        LibDummyValidator,
    )
except ImportError:

    class LibDummyValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class LibDummy:
    """Wrapper class for LibDummy Solidity contract."""

    def __init__(
        self,
        provider: BaseProvider,
        contract_address: str,
        validator: LibDummyValidator = None,
    ):
        """Get an instance of wrapper for smart contract.

        :param provider: instance of :class:`web3.providers.base.BaseProvider`
        :param contract_address: where the contract has been deployed
        :param validator: for validation of method inputs.
        """
        # pylint: disable=too-many-statements

        self.contract_address = contract_address

        if not validator:
            validator = LibDummyValidator(provider, contract_address)

        web3 = Web3(provider)

        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            for middleware in MIDDLEWARE:
                web3.middleware_onion.inject(  # type: ignore
                    middleware["function"], layer=middleware["layer"]
                )

        self._web3_eth = (
            web3.eth  # type: ignore # pylint: disable=no-member
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads("[]")  # noqa: E501 (line-too-long)


# pylint: disable=too-many-lines
