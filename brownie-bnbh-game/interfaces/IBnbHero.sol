// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

interface IBnbHero {
    function getPriceToUnlockLevel(uint256 _heroId) external view returns (uint256);

    // 打副本
    function fight(uint256 _heroId, uint256 enemyType) external;

    // 英雄升级
    function unLockLevel(uint256 _heroId) external;

    // reveal hero
    function expediteHero(uint256 _heroId) external;

    // claim 解锁时间
    function unLockTime(address _input) external view returns (uint256);

    // 查询地址累计获得的奖励
    function balances(address _input) external view returns (uint256);
}
