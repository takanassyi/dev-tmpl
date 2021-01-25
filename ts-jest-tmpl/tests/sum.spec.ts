import { sum } from '../src/sum';

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});

// describe-it の書き方でもよい
describe('sum() のテスト', () => {
  it('sum(1, 2) == 3', () => {
    expect(sum(1, 2)).toBe(3);
  });
});
