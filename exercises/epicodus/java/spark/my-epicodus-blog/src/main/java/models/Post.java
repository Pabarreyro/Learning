package models;

import java.time.LocalDateTime;
import java.util.ArrayList;

public class Post {

    private String title;
    private boolean published;
    private LocalDateTime createdAt;
    private static ArrayList<Post> instances = new ArrayList<>();
    private int id;

    public Post(String title) {
        this.title = title;
        this.published = false;
        this.createdAt = LocalDateTime.now();
        instances.add(this);
        this.id = instances.size();
    }

    public String getTitle() {
        return title;
    }

    public static ArrayList<Post> getAll() {
        return instances;
    }

    public static void clearAllPosts(){
        instances.clear();
    }

    public boolean isPublished() {
        return published;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public int getId() {
        return id;
    }

    public static Post findById(int id) {
        return instances.get(id-1);
    }
}
