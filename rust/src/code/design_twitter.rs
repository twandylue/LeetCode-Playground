use std::collections::{BinaryHeap, HashMap, HashSet};

type UserId = i32;
type TweetId = i32;
type Time = usize;

struct Twitter {
    time: Time,
    user_map: HashMap<UserId, HashSet<UserId>>,
    tweet_map: HashMap<UserId, Vec<(Time, TweetId)>>,
}

// /**
//  * `&self` means the method takes an immutable reference.
//  * If you need a mutable reference, change it to `&mut self` instead.
//  */
impl Twitter {
    fn new() -> Self {
        Twitter {
            time: 0,
            user_map: HashMap::new(),
            tweet_map: HashMap::new(),
        }
    }

    fn post_tweet(&mut self, user_id: i32, tweet_id: i32) {
        self.user_map.entry(user_id).or_insert(HashSet::new());
        self.tweet_map
            .entry(user_id)
            .and_modify(|v| v.push((self.time, tweet_id)))
            .or_insert(vec![(self.time, tweet_id)]);
        self.time += 1;
    }

    fn get_news_feed(&self, user_id: i32) -> Vec<i32> {
        let mut recents: Vec<TweetId> = Vec::new();
        let mut heap: BinaryHeap<(Time, TweetId)> = BinaryHeap::new();

        if let Some((k, hs)) = self.user_map.get_key_value(&user_id) {
            if let Some(tweets) = self.tweet_map.get(k) {
                heap.append(&mut BinaryHeap::from(tweets.to_owned()));
            }
            for u in hs.iter() {
                if let Some(tweets) = self.tweet_map.get(u) {
                    heap.append(&mut BinaryHeap::from(tweets.to_owned()));
                }
            }
        }

        for h in heap.into_sorted_vec().iter().rev().take(10) {
            recents.push(h.1);
        }

        recents
    }

    fn follow(&mut self, follower_id: i32, followee_id: i32) {
        self.user_map
            .entry(follower_id)
            .and_modify(|h| {
                h.insert(followee_id);
            })
            .or_insert(HashSet::from([followee_id]));
    }

    fn unfollow(&mut self, follower_id: i32, followee_id: i32) {
        self.user_map.entry(follower_id).and_modify(|h| {
            h.remove(&followee_id);
        });
    }
}

// /**
//  * Your Twitter object will be instantiated and called as such:
//  * let obj = Twitter::new();
//  * obj.post_tweet(userId, tweetId);
//  * let ret_2: Vec<i32> = obj.get_news_feed(userId);
//  * obj.follow(followerId, followeeId);
//  * obj.unfollow(followerId, followeeId);
//  */
#[cfg(test)]
mod tests {
    use super::Twitter;

    #[test]
    fn Twitter_case_1() {
        let mut tw = Twitter::new();
        tw.post_tweet(1, 5);
        let nt = tw.get_news_feed(1);
        assert_eq!(vec![5], nt);

        tw.follow(1, 2);
        tw.post_tweet(2, 6);
        let nt = tw.get_news_feed(1);
        assert_eq!(vec![6, 5], nt);

        tw.unfollow(1, 2);
        let nt = tw.get_news_feed(1);
        assert_eq!(vec![5], nt);
    }

    #[test]
    fn Twitter_case_2() {
        let mut tw = Twitter::new();
        tw.post_tweet(1, 5);
        tw.post_tweet(1, 3);
        tw.post_tweet(1, 101);
        tw.post_tweet(1, 13);
        tw.post_tweet(1, 10);
        tw.post_tweet(1, 2);
        tw.post_tweet(1, 94);
        tw.post_tweet(1, 505);
        tw.post_tweet(1, 333);

        let nt = tw.get_news_feed(1);
        assert_eq!(vec![333, 505, 94, 2, 10, 13, 101, 3, 5], nt);
    }
}
