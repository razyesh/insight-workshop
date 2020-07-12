
"""
Implementation of Tower of Hanoi
"""


def tower_of_hanoi(num_of_disk, from_pole, to_pole, helping_pole):
    """
    function to implement tower of hanoi problem for n disks
    :param num_of_disk: number of disk
    :param from_pole: starting pole
    :param to_pole: ending pole
    :param helping_pole: intermediate pole
    :return:
    """
    if num_of_disk <= 1:
        print("Put disk_{} from pole {} to pole {}".format(num_of_disk, from_pole, to_pole))
    else:
        tower_of_hanoi(num_of_disk-1, from_pole, helping_pole, to_pole)
        print("Put disk_{} from pole {} to pole {}".format(num_of_disk, from_pole, to_pole))
        tower_of_hanoi(num_of_disk-1, helping_pole, to_pole, from_pole)


if __name__ == "__main__":
    number_of_disk = int(input("Enter the number of disks: "))
    tower_of_hanoi(number_of_disk, 'A', 'C', 'B')