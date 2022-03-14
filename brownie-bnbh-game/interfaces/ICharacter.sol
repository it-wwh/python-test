// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

interface ICharacter {
    function balanceOf(address owner) external view returns (uint256);

    // 查询关卡的基础奖励 (0 ~ 6, 6: chapter1 boss)
    function baseBNBRewards(uint256 enemyId) external view returns (uint256);

    // 查询关卡的基础胜率
    function baseChances(uint256 enemyId) external view returns (uint256);

    // 查询关卡消耗的hp
    function requiredHps(uint256 enemyId) external view returns (uint256);

    // 查询hero的等级
    function getLevel(uint256 _heroId) external view returns (uint256);

    // 查询hero的当前hp,hp恢复的速度
    function getHpPoints(uint256 _heroId, bool calcTown) external view returns (uint256, uint256);

    function tokenOfOwnerByIndex(address owner, uint256 index) external view returns (uint256);

    function unLockLevel(uint256 _heroId) external view returns (uint256);

    function getHero(uint256 _heroId, bool calcTown) external view returns (uint256[6] memory a);
}
