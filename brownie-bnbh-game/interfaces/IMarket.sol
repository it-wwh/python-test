// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

interface IBnbHeroMarket {
    function getAllTokenIds() external view returns (uint256[] memory a);

    function getCharacterDataById(uint256 tokenId) external view returns (uint256[12] memory a);

    function purchaseListing(uint256 heroId) external;
}
