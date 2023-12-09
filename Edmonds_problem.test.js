it('pass: with a single digit number', function () {
   expect(printInReverse(9)).toEqual('printing completed');
});

it('pass: with a number with 2+ digits', function () {
  expect(printInReverse(19)).toEqual('printing completed');
  expect(printInReverse(10)).toEqual('printing completed');
  expect(printInReverse(345)).toEqual('printing completed');
  expect(printInReverse(1047)).toEqual('printing completed');
});

it('fail: input is a string', function () {
  expect(printInReverse("cats")).toEqual(undefined);
});