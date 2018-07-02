package models;

import javafx.geometry.Pos;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.time.LocalDateTime;

import static org.junit.Assert.*;

public class PostTest {

    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
        Post.clearAllPosts();
    }

    @Test
    public void newPost_instantiatesProperly_true() throws Exception{
        Post testPost = setupNewPost();
        assertEquals("Day 1: Intro", testPost.getTitle());
    }

    @Test
    public void newPost_newPostAddedToInstances_true() throws Exception{
        Post post = setupNewPost();
        Post otherPost = new Post ("How to pair successfully");
        assertEquals(2, Post.getAll().size());
    }

    @Test
    public void newPost_instantiatesWithPublishSetToFalse_false() throws Exception{
        Post testPost = setupNewPost();
        assertEquals(false, testPost.isPublished());
    }

    @Test
    public void newPost_instantiatesCurrentDateTime_today() throws Exception {
        Post testPost = setupNewPost();
        assertEquals(LocalDateTime.now().getDayOfWeek(), testPost.getCreatedAt().getDayOfWeek());
    }

    @Test
    public void newPost_instantiatesWithId_1() throws Exception{
        Post.clearAllPosts();
        Post testPost = setupNewPost();
        assertEquals(1, testPost.getId());
    }

    @Test
    public void getAll_allPostInstancesReturned_true() throws Exception{
        Post post = setupNewPost();
        Post otherPost = new Post ("How to pair successfully");
        assertTrue(Post.getAll().contains(post));
        assertTrue(Post.getAll().contains(otherPost));
    }

    @Test
    public void findById_returnsCorrectPost_1() throws Exception{
        Post testPost = setupNewPost();
        assertEquals(1, testPost.findById(testPost.getId()).getId());
    }

    @Test
    public void findById_returnsCorrectSecondPost_2() throws Exception{
        Post post = setupNewPost();
        Post otherPost = new Post ("How to pair successfully");
        assertEquals(2, otherPost.findById(otherPost.getId()).getId());
    }

    public Post setupNewPost() throws Exception{
        return new Post("Day 1: Intro");
    }
}