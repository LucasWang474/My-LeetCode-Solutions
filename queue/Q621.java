public class Q621 {
    public int leastInterval(char[] tasks, int n) {
        int[] counts = new int[26];
        int max = 0, maxDuplicate = 0;
        for (char c : tasks) {
            counts[c - 'A']++;
            int current = counts[c - 'A'];
            if (current == max) {
                maxDuplicate++;
            } else if (current > max) {
                max = current;
                maxDuplicate = 1;
            }
        }

        int parts = max - 1;
        int emptySlots = parts * (n - maxDuplicate + 1);
        int availableTasks = tasks.length - maxDuplicate * max;
        int idles = Math.max(0, emptySlots - availableTasks);
        return tasks.length + idles;
    }
}
