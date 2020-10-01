#include <bits/stdc++.h>
using namespace std;

void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
    return;
}

int segregate(vector<int> &arr)
{
    int j = 0;
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] <= 0)
        {
            swap(&arr[i], &arr[j]);
            j++;
        }
    }
    return j;
}

int findMissingPositive(vector<int> &arr)
{
    int size = arr.size();
    for (int i = 0; i < size; i++)
    {
        if (abs(arr[i]) - 1 < size && arr[abs(arr[i]) - 1] > 0)
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1];
    }

    for (int i = 0; i < size; i++)
        if (arr[i] > 0)
            return i + 1;

    return size + 1;
}

int findMissing(vector<int> &arr)
{
    int shift = segregate(arr);
    vector<int> shiftedvector;
    for (int i = shift; i < arr.size(); i++)
        shiftedvector.push_back(arr[i]);
    cout << "shifted vector\n";
    for (int i = 0; i < shiftedvector.size(); i++)
        cout << shiftedvector[i] << " ";
    cout << endl;
    return findMissingPositive(shiftedvector);
}

int firstMissingPositive(vector<int> &A)
{
    int ans = findMissing(A);
    return ans;
}

int main()
{
    // int n;
    // cin >> n;
    // vector<int> A(n);
    // for (int i = 0; i < n; i++)
    //     cin >> A[i];
    vector<int> A = {948, 20, 84, 710, 471, 606, 995, 581, -4, 428, 149, 832, 740, 943, 450, 974, 829, 721, 821, 476, 763, 4, 523, 937, 814, 624, 935, 87, 127, 816, 239, 33, 561, 999, 904, 282, 844, 923, 750, 551, 432, 9, 373, 387, 114, 376, 265, 801, 228, 454, 474, 764, 268, 680, 472, 431, 133, 785, 752, 643, 441, 151, 969, 395, 437, 94, 259, 973, 535, 272, 456, 546, 79, 677, 0, 109, 522, 295, 466, 956, 723, 157, 772, 865, 997, 771, 922, 980, 567, 939, 651, 478, 852, 926, 913, 494, 882, 207, 915, 645, 754, 385, 874, 554, 706, 722, 10, 374, 96, 647, 280, 418, 737, 538, 867, 850, 600, 23, 730, 742, 224, 511, 361, 251, 809, 907, 271, 319, 866, 848, 594, 566, 113, 211, 334, 644, 826, 430, 929, 603, 165, 147, 788, 529, 539, 633, 275, 602, 544, 540, 853, 123, -1, 443, 942, 386, 68, 465, 782, 250, 458, 174, 70, 919, 462, 347, 26, 589, 880, 648, 237, 294, 641, 707, 516, 507, 802, 989, 779, 519, 62, 619, 584, 358, 362, 277, 43, 198, 467, 625, 611, 212, 468, 767, 778, 173, 791, 331, 11, 461, 572, 97, 902, 558, 413, 28, 179, 370, 842, 568, 500, 311, 550, 464, 345, 411, 274, 181, 396, 339, 39, 760, 575, 327, 889, 579, 840, 734, 254, 934, 532, 29, 622, 780, 73, 479, 322, 2, 599, 227, 685, 65, 510, 716, 289, 912, 574, 262, 916, 924, 304, 57, 353, 40, 341, 521, 131, 307, 526, 398, 225, 63, 776};
    int ans = firstMissingPositive(A);
    cout << ans << endl;
    return 0;
}
