// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

contract messySpeaker {

    uint256 public  HighestPrice;
    uint256 public  gap;
    string  public  something;
    address private admin;

    event aPayment(address buyer, uint256 price, string say_sth);

    constructor (string memory _sth) {
        admin = msg.sender;
        HighestPrice = 0;
        gap = 0.0005 ether;
        something = _sth;
    }

    modifier onlyAdmin {
        require(msg.sender == admin);
        _;
    }

    function pay_me_and_say_sth(string memory _say_sth) public payable {
        require(msg.value >= HighestPrice + gap, 'Incorrect value sent');

        payable(admin).transfer(msg.value);
        something = _say_sth;
        HighestPrice = msg.value;

        emit aPayment(msg.sender, msg.value, _say_sth);
    }

    function what_do_you_say() external view returns (string memory) {
        return something;
    }

    function now_price() external view returns (uint256) {
        return HighestPrice;
    }

    function now_gap() external view returns (uint256) {
        return gap;
    }

    function setPrice(uint256 _price) external onlyAdmin {
        HighestPrice = _price;
    }

    function setGap(uint256 _gap) external onlyAdmin {
        gap = _gap;
    }

}